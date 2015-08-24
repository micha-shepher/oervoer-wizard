'''
Created on 21 sep. 2014

@author: mshepher

prototype of a picklist wizard for www.oervoer.nl
'''
import os


from delivery import Delivery
from decimal import Decimal
from weighted_random import WeightedRandom
import csv
import numpy
from numpy.lib.function_base import median
from wizard.models import Order, Globals, MeatType, Product, Taste
                   
class NoProductsException(Exception):
    def __init__(self, desc, l=None, weight=None):
        self.l = l
        self.weight = weight
        self.desc = desc
    def __str__(self):
        return self.desc
    def __desc__(self):
        return self.desc
                
class Oervoer(object):
    def __init__(self,productname, ordername, picklistname):
        '''initialize the inputs'''
        self.prodlists = {}
        self.ordlist   = Order.objects.filter(status__in = ('processing','pending'))
        self.exceptions = []
        self.random = False
        self.products = Product.objects.all()
        self.meattypes = MeatType.objects.all()
    
    def set_globals(self, id):
        try:
            self.globals = Globals.objects.get(pk=id)
        except Globals.DoesNotExist:
            self.globals = Globals.objects.all()[0]
            
    def set_random(self, state):
        self.random = state
        
    def parse_products(self):
        '''get the products in the lists
        '''
        for prod in self.products:
            if self.prodlists.has_key(prod.vlees):
                self.prodlists[prod.vlees].append(prod)
            else:
                self.prodlists[prod.vlees] = [prod]
        
    def dump(self):
        '''prove that there is a picklist'''
        for i in self.prodlists.keys():
            print "produkt klasse: %s, aantal produkten: %d" % (i,len(self.prodlists[i]))

    def product_ok_for_catdog(self, pr, catdog):
        return catdog.upper() in pr.kat_hond
    
    def make_list(self, vlees, order, meal_size):
        '''get rid of products too big for the animal
        or untasteful to the animal.
        Since cats often have meals smaller than 100gr, raise an exception.'''
        outlist = []
        # make a distinction between hard and soft bone
        profile = order.pet.profile
        donts = order.pet.donts_set.all()
        
        deelbaar = vlees in ['BOT', 'GEMALEN', 'ORGAAN', 'PENS', 'SPIER'] 
        if deelbaar:
            fact1 = profile.MEALFACTOR
            fact2 = profile.MEALFACTOR2
        else:
            fact1 = profile.MEALFACTOR3
            fact2 = 0.0
        thelist = []
        if vlees == 'BOT':
            if order.pet.is_hond():
                for _vlees in (MeatType.objects.filter(meat_type__in = ('HARD BOT', 'MIDDEL BOT', 'ZACHT BOT'))):
                    try:
                        thelist += self.prodlists[_vlees]
                    except KeyError:
                        pass
            else:
                thelist = self.prodlists[MeatType.objects.get(meat_type='ZACHT BOT')]
        elif vlees == 'VIS':
            for _vlees in MeatType.objects.filter(meat_type__contains = 'VIS'):
                try:
                    thelist += self.prodlists[_vlees]
                except KeyError:
                    pass
        elif vlees == 'COMPLEET KARKAS':
            if order.pet.is_hond():
                for _vlees in MeatType.objects.filter(meat_type__contains = 'KARKAS'):
                    try:
                        thelist += self.prodlists[_vlees]
                    except KeyError:
                        pass
            else:
                thelist += self.prodlists[MeatType.objects.get(meat_type='COMPLEET KARKAS.ZACHT BOT')]    
        elif vlees == 'GEMALEN':
            for _vlees in MeatType.objects.all():
                if _vlees.is_gemalen:
                    try:
                        thelist += self.prodlists[MeatType.objects.get(meat_type=_vlees)]
                    except KeyError:
                        pass
        elif vlees == 'PENS':
            thelist = self.prodlists[MeatType.objects.get(meat_type='PENS')]
        elif vlees == 'ORGAAN':
            thelist = self.prodlists[MeatType.objects.get(meat_type='ORGAAN')]
        else:
            thelist = self.prodlists[MeatType.objects.get(meat_type=vlees)]


        thelist.sort(key=lambda prod: prod.get_norm_weight()) # work with products sorted by normalized weight
        print 'total products in list for {} = {}'.format(vlees, len(thelist))

        print 'prod, condition, not in dontslist, is disjoint, ras OK'
        for pr in thelist:
            condition = pr.get_norm_weight() <= meal_size * fact1 and \
                        pr.get_norm_weight() >= meal_size * fact2
            if pr.vlees.is_gemalen:
                if abs(profile.MEAL - profile.BIGMEAL) < 50 or abs(profile.MEAL - profile.SMALLMEAL) < 50:
                    condition = abs(pr.get_norm_weight() - Decimal(profile.MEAL/1000.0)) < 0.05
                else:
                    pass

            dontslist = [t.taste for t in donts]
            print '{:>25}{:>6}{:>6}{:>6}{:>6}{:>6}'.format(pr.sku, 
                condition, 
                not (pr.smaak in dontslist), 
                set(pr.smaak.taste.split('.')).isdisjoint(set ([t.taste for t in donts])), 
                self.product_ok_for_catdog(pr, order.pet.ras.ras), pr.qty)
            if condition and \
               (not (pr.smaak in dontslist)) and \
               (pr.qty > 0) and \
               set(pr.smaak.taste.split('.')).isdisjoint(set (dontslist)) and\
               (not pr.vlees.meat_type in dontslist) and\
               self.product_ok_for_catdog(pr, order.pet.ras.ras):
                outlist.append(pr)

        if len(outlist) == 0:
            # try again, choose products smaller than or greater than...
            print "no products found for {0}".format(vlees)
            if meal_size * fact1 < thelist[0].get_norm_weight(): # too small!
                thelist = [p for p in thelist if p.get_norm_weight() <= (profile.SMALLMEAL+50)/1000.0]
            else:
                thelist = [p for p in thelist if p.get_norm_weight() >= (profile.BIGMEAL-50)/1000.0]
                
            for pr in thelist:
                if (not (pr.smaak in dontslist)) and \
                   (not (pr.smaak.taste.split('.')[0] in dontslist)) and \
                   pr.qty > 0 and \
                   (not pr.vlees.meat_type in dontslist):
                    outlist.append(pr)
                
        quantities = []
        if len(outlist) == 0:
            raise NoProductsException('Lijst van potentieele {} producten voor {} is leeg.'.format(vlees, order.pet))
        for p in outlist:
            if self.random:
                quant = p.get_qty()
            else:
                quant = 1
            if p.smaak in order.pet.prefers_set.all():
                quantities.append(quant*profile.LIKEFACTOR)
            else:
                quantities.append(quant)    
        return WeightedRandom(quantities), outlist
    
    def fill(self, order, wr, prodlist, weight, vleessoort ):
        ''' fill a list with products of the soort '''
        profile = order.pet.profile
        donts = order.pet.donts_set.all()
        def is_fishhead(prod):
            ''' take care that only one fish head is appended to list'''
            tup = prod.smaak.taste.split('.')
            return len(tup) > 1 and tup[1] == profile.HEAD

        l = []
        total_weight = 0.0
        fish_head_in_list = False
        meattype = MeatType.objects.filter(meat_type__contains = (vleessoort))[0]
        try:
            # force selection of liver if orgaan
            if meattype.is_orgaan:
                tries = 0
                while total_weight < weight and tries < profile.tries:
                    tries += 1
                    prod = prodlist[wr.rand()]
                    if prod.smaak in donts:
                        print '{0} in donts, isliver={1}, rejected!'.format(prod.sku, prod.smaak.is_liver)
                        continue

                    if (total_weight <= weight * profile.LEVERDEEL and prod.smaak.is_liver) or\
                        (total_weight >  weight * profile.LEVERDEEL and not prod.smaak.is_liver):
                        total_weight += float(prod.weight)
                        l.append(prod)
                        print 'appended {0} weight {1}'.format(prod.sku, total_weight)
                    if total_weight >= weight:
                        break
                if tries >= profile.tries:
                    print 'orgaan error! cant fulfill requirements for {}'.format(order.pet)
                        
            # complete the filling
            else:
                toomany = 0
                while total_weight < weight and not toomany > profile.REPEATS:
                    toomany += 1
                    prod = prodlist[wr.rand()]
                    isfh = is_fishhead(prod)
                    if not (isfh and fish_head_in_list):
                        total_weight += float(prod.weight)
                        l.append(prod)
                    if isfh:
                        fish_head_in_list = True
                if toomany > profile.REPEATS:
                    print 'failed to fill {}, w {}, len {}'.format(vleessoort, total_weight, len(l))
                    raise NoProductsException('Kan lijst {0} niet voldoen, misschien pakket te groot of viskop rule?'.format(vleessoort),
                                              l, total_weight)
        except ValueError:
            raise NoProductsException('Niet genoeg producten voor type %s' % vleessoort,
                                      l, total_weight)    
            #print 'selected %s, total=%s, %s to go' % (prod.name, total_weight, minimum_items-len(l))
        return total_weight, l
     
    def totalqty(self, l):
        '''returns how many products total in the product list inventory'''
        s = 0
        for i in l:
            s += i.get_qty()
        return s

    def choose_best(self, l, qty, to_reach_weight):
        #print 'length original: {}'.format(len(l))
        tlist = []
        for ind, sel in enumerate(l):
            tastes = {} # dict with tastes in this list of products. taste:number
            for prod in sel:
                smaak = prod.smaak
                if tastes.has_key(smaak):
                    tastes[smaak] += float(prod.weight)
                else:
                    tastes[smaak] = float(prod.weight)
            
            tlist.append([ind,tastes,0])
        tlist.sort(key=lambda x: len(x[1])) # tlist is now sorted by most tastes.
        # now get the sub list of all selections containing more than the median.
        #print tlist
        arr = [len(t[1]) for t in tlist]
        median = numpy.median(arr)
        print 'median number of tastes is {}'.format(median)
        #final = [x for x in tlist if len(x[1])>=median]
        
        final = []
        for ind, sel in enumerate(tlist):
            weightdev = abs(to_reach_weight-sum(sel[1].values()))
            if len(sel[1]) >= median and\
                weightdev <= to_reach_weight * 0.25:
                final.append(sel)
        for selection in final:
            std = numpy.std(selection[1].values())
            selection[2] = std
        
        final.sort(key=lambda x: x[2])

        #for x in range(len(final)):
        #    print final[x]
        
        if len(final) == 0:
            print '''something wrong happened when looking for best selection, resulting in no solutions.'''
            print 'original length: {}({})'.format(len(l), len(tlist))
            print 'median:', median
            return l[tlist[0][0]]
        else:
            return l[final[0][0]]    
                
    def select_type(self, meal_type, order, meal_size, to_reach_weight):
        wr, typlist = self.make_list(meal_type, order, meal_size)
        
        l = []
        qty = []
        for _ in xrange(order.pet.profile.tries):
            x, y =  self.fill(order, wr, typlist, to_reach_weight, meal_type)
            qty.append(x)
            l.append(y)
            
        #total = min(qty, key=lambda x: abs(to_reach_weight - x)) # minimize delta from target weight
        #selection = l[ qty.index(total) ]
        selection = self.choose_best(l,qty,to_reach_weight)
        #print [x.sku for x in selection]
        return sum([float(x.weight) for x in selection]), selection
        
    def make_plus(self, order):
        '''gemalen + pens + stukjes vis
        vis 1/7 van een menu
        pens 1/7 van een menu if hond
        gemalen 5/7 van een menu'''
        
        #days = order.get_days()
        meal_size = order.pet.get_meal_size()
        #days_met_vis = round(days / 7)  # wat gebeurt als days<7???
        package_rest = float(order.weight)
        
        donts = order.pet.donts_set.all()
        ##############################
        # select vis
        ##############################
        products_in_order = []
        try:
            total_vis, products_in_order = self.select_type('VIS', order, meal_size, package_rest * 0.15)
            package_rest -= total_vis
        except NoProductsException, e:
            self.exceptions.append(('VIS', order.pet, e))
            if e.l:
                total_vis = e.weight
                products_in_order = e.l
            
        ##############################
        # select pens if not kat
        ##############################
        if order.pet.is_hond() and not 'PENS' in [d.taste for d in donts]:
            try:
                total_pens, selection = self.select_type('PENS', order, meal_size, float(order.weight) * 0.15)
                products_in_order.extend(selection)
                package_rest -= total_pens
            except NoProductsException, e:
                self.exceptions.append(('PENS', order.pet, e))
                if e.l:
                    total_pens = e.weight
                    products_in_order = e.l
            
            
        ##############################
        # select gemalen
        ##############################
        try:
            _, selection = self.select_type('GEMALEN', order, meal_size, package_rest)
            products_in_order.extend(selection)
        except NoProductsException, e:
            self.exceptions.append(('GEMALEN', order.pet, e))
        return products_in_order
                     
    def update_inventory(self, result, howmuch = 1):
        for resprod in result:
            for prod in self.prodlists[resprod.get_type()]:
                if resprod.sku == prod.sku:
                    prod.qty -= howmuch
                    # print '%s was %d, now %d' %(prod.sku, prod.qty+1, prod.qty)b
 
    def correct_result(self, order, result):
        '''try to fix the result by removing products that are not unique and make the package too heavy.
        look for products whose weight approximates the difference or the total weight from the package weight'''
        
        weights = [float(i.weight) for i in result] # weight vector
        pckg = float(order.weight)
        looking4 = abs(pckg-sum(weights))          # looking for a product weighing about that.
        if looking4 < 0.05 or sum(weights) < pckg: # not worth fixing if it ain't broke
            print 'afwijking {0}'.format(looking4)
            return # nothing to do
        min_val = min([abs(i-looking4) for i in weights]) # difference between closest product and delta in package.
        
        length = len(result)
        # search for candidates for deletion
        for i,j in enumerate(weights):
            if abs(j-looking4) == min_val:
                if [p.sku for p in result].count(result[i].sku) > 1: # if the product is not unique
                    result.pop(i)
                    break
        
                           
    def process_order(self, order):
        '''make a picklist from the products and the order'''
        if order.package.type == 'PLUS':
            result = self.make_plus(order)
        elif order.package.type == 'COMBI':
            result = self.make_combi(order)
        else:
            result = self.make_100(order)
        self.correct_result(order, result)
        #if order.result: # fix inventory after discarded order
        #    self.update_inventory(order.result, -1)
        #self.update_inventory(result)
        #order.set_result(result)
        return result

    def make_combi(self, order):
        order.weight /= Decimal(2.0)
        result = self.make_100(order)+self.make_plus(order)
        order.weight *= Decimal(2.0)
        return result
    
    def make_100(self, order):
        '''ongemalen compleet + ongemalen incompleet + pens + stukjes vis
        vis 1/7 van een menu
        pens 1/7 van een menu if hond
        5/14 of 6/14 ongemalen incompleet
        5/14 of 6/14 ongemalen compleet
        '''
        
        #days = order.get_days()
        self.dump()
        meal_size = order.pet.get_meal_size()
        #days_met_vis = round(days / 7)  # wat gebeurt als days<7???
        package_rest = float(order.weight)
        ##############################
        # select vis
        ##############################
        products_in_order = []
        
        total_vis = 0.0
        try:
            total_vis, products_in_order = self.select_type('VIS', order, meal_size, package_rest*0.15)
            package_rest -= total_vis
        except NoProductsException, e:
            self.exceptions.append(('VIS', order.pet, e))
            if e.l:
                total_vis = e.weight
                products_in_order = e.l
            
        ##############################
        # select pens if not kat
        ##############################
        total_pens = 0.0
        if (not order.pet.is_kat()) and not 'PENS' in order.pet.donts_set.all():
            try:
                total_pens, selection = self.select_type('PENS', order, meal_size, float(order.weight)*0.15)
                products_in_order.extend(selection)
                package_rest -= total_pens
            except NoProductsException, e:
                self.exceptions.append(('PENS', order.pet, e))
                
            
        ##############################
        # select ongemalen compleet
        ##############################
        total_compleet_karkas = 0.0
        try:
            total_compleet_karkas, selection = self.select_type('COMPLEET KARKAS', order, meal_size, package_rest/2.0)
            products_in_order.extend(selection)
            package_rest -= total_compleet_karkas
        except NoProductsException, e:
            self.exceptions.append(('COMPLEET KARKAS', order.pet, e))
        
        #################################
        # select ongemalen incompleet orgaan
        #################################
        total_orgaan = 0.0
        try:
            total_orgaan, selection = self.select_type('ORGAAN', order, meal_size, package_rest*0.15)
            products_in_order.extend(selection)
        except NoProductsException, e:
            self.exceptions.append(('ORGAAN', order.pet, e))
            total_orgaan = 0
        
        ###################################
        # select ongemalen incompleet spier
        ###################################
        total_spier = 0.0
        try:
            total_spier, selection = self.select_type('SPIERVLEES', order, meal_size, package_rest*0.4)
        except NoProductsException, e:
            self.exceptions.append(('SPIERVLEES', order.pet, e))
            total_spier = 0
            selection = []
        
        products_in_order.extend(selection)
        package_rest -= (total_spier+total_orgaan)
        ####################################
        # select ongemalen incompleet bot
        ####################################
        total_bot = 0.0
        try:
            total_bot, selection = self.select_type('BOT', order, meal_size, package_rest)
        except NoProductsException, e:
            self.exceptions.append(('BOT', order.pet, e))
            selection = []
        
        products_in_order.extend(selection)
        pkg = float(order.weight)/100.0
        print 'vis,pens,kark,spier,orgaan,bot', total_vis, total_pens, total_compleet_karkas, total_spier,\
                                                total_orgaan, total_bot
        print 'vis,pens,kark,spier,orgaan,bot', total_vis/pkg, total_pens/pkg, total_compleet_karkas/pkg,\
                                                total_spier/pkg, total_orgaan/pkg, total_bot/pkg
        return products_in_order
        
    def write_inventory(self):
        import csv
        name = '.'.join(self.productname.split('.')[:-1])+'.new.csv'
        
        f = file(name, 'w')
        fcsv = csv.writer(f)
        fcsv.writerow('store sku qty is_in_stock geschiktmenu name smaak type_vlees shelf weight'.split())
        
        for prodtype in self.prodlists.values():
            for prod in prodtype:
                fcsv.writerow (['admin', prod.sku, prod.qty, 1, 'Ja', prod.name, prod.smaak, prod.type, prod.shelf, prod.weight])
             
                
if __name__ == '__main__':
    import django
    django.setup()
    testdir = os.getenv('OERVOERTESTENV') 
    if not testdir:
        testdir = '../test/'
    oervoer = Oervoer(testdir+'products.csv',testdir+'orders.csv',testdir+'picklists.csv')
    oervoer.parse_products()
    oervoer.parse_orders()
    for order in oervoer.ordlist:
        try:
            result = oervoer.process_order(order)
            d = Delivery(testdir, order, result)
            print d.csvout()
            oervoer.write_inventory()
        except NoProductsException,e:
            print e
            print '%s\nKan order %s-%s niet vervullen.\n%s\n' % ('^'*70, order.owner, order.animal,'#$'*35 )
    oervoer.dump()
