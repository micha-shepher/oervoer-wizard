'''
Created on 21 sep. 2014

@author: mshepher

prototype of a picklist wizard for www.oervoer.nl
'''
import os


from order import Order
from product import Product
from globals import Globals
from delivery import Delivery
from weighted_random import WeightedRandom
import csv
import numpy
from numpy.lib.function_base import median
                   
class NoProductsException(Exception):
    def __init__(self, desc, l=None, weight=None):
        self.l = l
        self.weight = weight
        self.desc = desc
    def __str__(self):
        return self.desc
                
class Oervoer(object):
    def __init__(self,productname, ordername, picklistname):
        '''initialize the inputs'''
        self.productname = productname
        self.products  = csv.DictReader(file(productname,  'r'))
        self.prodlists = {}
        orderlines = file(ordername,    'r').readlines()
        self.orderhead = orderlines.pop(0)
        self.orders = orderlines
        self.picklists = file(picklistname, 'w')
        self.ordlist   = []
        self.exceptions = []
        self.random = False
        for i in Globals.VLEES_TYPES:
            self.prodlists[i] = []
    
    def set_random(self, state):
        self.random = state
        
    def parse_products(self):
        '''get the products in the lists
        '''
        for prod in self.products:
            p = Product(prod) # prod is a dictionary
            p.dump()
            if p.get_type() in Globals.VLEES_TYPES and p.get_include() and p.get_qty() > 0:
                self.prodlists[p.get_type()].append(p)
        for x in self.prodlists.keys():
            print x, len(self.prodlists[x])
    
    def parse_orders(self):
        '''get the products in the lists
        '''
        for order in self.orders:
            self.ordlist.append(Order(order))
        return self.ordlist
    
    def dump(self):
        '''prove that there is a picklist'''
        for i in self.prodlists.keys():
            print "produkt klasse: %s, aantal produkten: %d" % (i,len(self.prodlists[i]))
        for i in self.ordlist:
            print i.owner, i.ras, i.animal, i.get_package(), i.get_kind()

    def make_list(self, vlees, order, meal_size):
        '''get rid of products too big for the animal
        or untasteful to the animal.
        Since cats often have meals smaller than 100gr, raise an exception.'''
        outlist = []
        # make a distinction between hard and soft bone
        if vlees in Globals.VLEES_DEELBAAR:
            fact1 = Globals.MEALFACTOR
            fact2 = Globals.MEALFACTOR2
        else:
            fact1 = Globals.MEALFACTOR3
            fact2 = 1.0/Globals.MEALFACTOR3
        if vlees == Globals.BOT:
            if order.ras == 'HOND':
                thelist = []
                for taste in (Globals.ZACHTBOT, Globals.MIDDELBOT, Globals.HARDBOT):
                    thelist += self.prodlists[taste]
            else:
                thelist = self.prodlists[Globals.ZACHTBOT]
        elif vlees == Globals.VIS:
            thelist = self.prodlists[Globals.VIS] + self.prodlists[Globals.VISGEMALEN]
        elif vlees == Globals.KARKAS:
            thelist = []
            for taste in Globals.KARKAS_DICT[order.ras]:
                thelist += self.prodlists[taste]
        else:
            thelist = self.prodlists[vlees]
        thelist.sort(key=lambda prod: prod.get_norm_weight()) # work with products sorted by normalized weight
        for vl in thelist:
            if vlees == Globals.GEMALEN and order.get_portie() == 'grote porties':
                condition = vl.get_norm_weight() >= Globals.BIGMEAL/1000.0
            elif vlees == Globals.GEMALEN and order.get_portie() == 'kleine porties':
                condition = vl.get_norm_weight() <= Globals.SMALLMEAL/1000.0
            else:
                condition = vl.get_norm_weight() <= meal_size * fact1 and \
                            vl.get_norm_weight() >= meal_size * fact2
            if vlees == Globals.ORGAAN:
                pass # prepare a breakpoint.
            if  condition and \
               not (vl.smaak in order.donts) and             \
               not (vl.smaak.split('.')[0] in order.get_donts()) and \
               not (vl.get_type() in order.get_donts()) and \
               set(vl.smaak.split('.')).isdisjoint(set (order.get_donts()) ) and\
               vl.get_kathond(order.ras):
                outlist.append(vl)
        if len(outlist) == 0:
            # try again, choose products smaller than or greater than...
            print "no products found for {0}".format(vlees)
            if meal_size * fact1 < thelist[0].get_norm_weight(): # too small!
                thelist = [p for p in thelist if p.get_norm_weight() <= Globals.SMALLMEAL]
            else:
                thelist = [p for p in thelist if p.get_norm_weight() >= Globals.BIGMEAL]
                
            for vl in thelist:
                if not (vl.smaak in order.donts) and \
                   not (vl.smaak.split('.')[0] in order.donts):
                        outlist.append(vl)
                
        quantities = []
        for p in outlist:
            if self.random:
                quant = p.get_qty()
            else:
                quant = 1
            if p.smaak in order.get_prefers():
                quantities.append(quant*Globals.LIKEFACTOR)
            else:
                quantities.append(quant)    
        return WeightedRandom(quantities), outlist
    
    def fill(self, order, wr, prodlist, weight, vleessoort ):
        ''' fill a list with products of the soort '''
        def is_fishhead(prod):
            ''' take care that only one fish head is appended to list'''
            tup = prod.smaak.split('.')
            return len(tup) > 1 and tup[1] == Globals.HEAD

        l = []
        total_weight = 0.0
        fish_head_in_list = False
        try:
            # force selection of liver if orgaan
            if vleessoort == Globals.ORGAAN:
                tries = 0
                maxtries = 20
                while total_weight < weight and tries < maxtries:
                    for prod in prodlist:
                        if prod.smaak in order.get_donts():
                            continue
                        liver_found = prod.smaak.find(Globals.LEVER) > -1
                        if (total_weight <= weight * Globals.LEVERDEEL and liver_found) or\
                            (total_weight >  weight * Globals.LEVERDEEL and not liver_found):
                            total_weight += prod.get_weight()
                            l.append(prod)
                        if total_weight >= weight:
                            break
                        
            # complete the filling
            else:
                toomany = 0
                while total_weight < weight and not toomany > Globals.maxtries:
                    toomany += 1
                    prod = prodlist[wr.rand()]
                    isfh = is_fishhead(prod)
                    if not (isfh and fish_head_in_list):
                        total_weight += prod.get_weight()
                        l.append(prod)
                    if isfh:
                        fish_head_in_list = True
                if toomany > Globals.maxtries:
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
        tlist = []
        for ind, sel in enumerate(l):
            tastes = {} # dict with tastes in this list of products. taste:number
            for prod in sel:
                smaak = prod.smaak
                if tastes.has_key(smaak):
                    tastes[smaak] += prod.get_weight()
                else:
                    tastes[smaak] = prod.get_weight()
            
            tlist.append([ind,tastes,0])
        tlist.sort(key=lambda x: len(x[1])) # tlist is now sorted by most tastes.
        # now get the sub list of all selections containing more than the median.
        arr = [len(t[1]) for t in tlist]
        median = numpy.median(arr)
        
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
            print 'original length: {}'.format(len(tlist))
            print 'deviation:', weightdev
            print 'median:', median
            
            return l[tlist[0][0]]
        else:
            return l[final[0][0]]    
                
    def select_type(self, meal_type, order, meal_size, to_reach_weight):
        wr, typlist = self.make_list(meal_type, order, meal_size)
        
        l = []
        qty = []
        for _ in xrange(Globals.tries):
            x, y =  self.fill(order, wr, typlist, to_reach_weight, meal_type)
            qty.append(x)
            l.append(y)
            
        #total = min(qty, key=lambda x: abs(to_reach_weight - x)) # minimize delta from target weight
        #selection = l[ qty.index(total) ]
        selection = self.choose_best(l,qty,to_reach_weight)
        #print [x.sku for x in selection]
        return sum([x.get_weight() for x in selection]), selection
        
    def make_plus(self, order):
        '''gemalen + pens + stukjes vis
        vis 1/7 van een menu
        pens 1/7 van een menu if hond
        gemalen 5/7 van een menu'''
        
        #days = order.get_days()
        meal_size = order.get_meal_size()
        #days_met_vis = round(days / 7)  # wat gebeurt als days<7???
        package_rest = order.get_package()
        ##############################
        # select vis
        ##############################
        products_in_order = []
        try:
            total_vis, products_in_order = self.select_type('VIS', order, meal_size, package_rest * 0.15)
            package_rest -= total_vis
        except NoProductsException, e:
            self.exceptions.append(('VIS', order.get_animal(), e))
            if e.l:
                total_vis = e.weight
                products_in_order = e.l
            
        ##############################
        # select pens if not kat
        ##############################
        if order.ras != 'KAT' and not 'PENS' in order.donts:
            try:
                total_pens, selection = self.select_type('PENS', order, meal_size, order.get_package() * 0.15)
                products_in_order.extend(selection)
                package_rest -= total_pens
            except NoProductsException, e:
                self.exceptions.append(('PENS', order.get_animal(), e))
                if e.l:
                    total_pens = e.weight
                    products_in_order = e.l
            
            
        ##############################
        # select gemalen
        ##############################
        try:
            _, selection = self.select_type('COMPLEET GEMALEN', order, meal_size, package_rest)
            products_in_order.extend(selection)
        except NoProductsException, e:
            self.exceptions.append(('COMPLEET GEMALEN', order.get_animal(), e))
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
        
        weights = [i.get_weight() for i in result] # weight vector
        pckg = order.get_package()
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
        print '%s\ninhoud pakket %s voor %s-%s\n%s' % ('-'*70, order.kind,order.owner,order.animal,'-'*70)
        if order.get_kind() == 'PLUS':
            result = self.make_plus(order)
        elif order.get_kind() == 'COMBI':
            result = self.make_combi(order)
        else:
            result = self.make_100(order)
        self.correct_result(order, result)
        if order.result: # fix inventory after discarded order
            self.update_inventory(order.result, -1)
        self.update_inventory(result)
        order.set_result(result)
        return result

    def make_combi(self, order):
        order.package /= 2.0
        result = self.make_100(order)+self.make_plus(order)
        order.package *= 2.0
        return result
    
    def make_100(self, order):
        '''ongemalen compleet + ongemalen incompleet + pens + stukjes vis
        vis 1/7 van een menu
        pens 1/7 van een menu if hond
        5/14 of 6/14 ongemalen incompleet
        5/14 of 6/14 ongemalen compleet
        '''
        
        #days = order.get_days()
        meal_size = order.get_meal_size()
        #days_met_vis = round(days / 7)  # wat gebeurt als days<7???
        package_rest = order.get_package()
        ##############################
        # select vis
        ##############################
        products_in_order = []
        
        total_vis = 0.0
        try:
            total_vis, products_in_order = self.select_type('VIS', order, meal_size, package_rest*0.15)
            package_rest -= total_vis
        except NoProductsException, e:
            self.exceptions.append(('VIS', order.get_animal(), e))
            if e.l:
                total_vis = e.weight
                products_in_order = e.l
            
        ##############################
        # select pens if not kat
        ##############################
        total_pens = 0.0
        if order.ras != 'KAT' and not 'PENS' in order.donts:
            try:
                total_pens, selection = self.select_type('PENS', order, meal_size, order.get_package()*0.15)
                products_in_order.extend(selection)
                package_rest -= total_pens
            except NoProductsException, e:
                self.exceptions.append(('PENS', order.get_animal(), e))
                
            
        ##############################
        # select ongemalen compleet
        ##############################
        total_compleet_karkas = 0.0
        try:
            total_compleet_karkas, selection = self.select_type('COMPLEET KARKAS', order, meal_size, package_rest/2.0)
            products_in_order.extend(selection)
            package_rest -= total_compleet_karkas
        except NoProductsException, e:
            self.exceptions.append(('COMPLEET KARKAS', order.get_animal(), e))
        
        #################################
        # select ongemalen incompleet orgaan
        #################################
        total_orgaan = 0.0
        try:
            total_orgaan, selection = self.select_type('ORGAAN', order, meal_size, package_rest*0.15)
            products_in_order.extend(selection)
        except NoProductsException, e:
            self.exceptions.append(('ORGAAN', order.get_animal(), e))
            total_orgaan = 0
        
        ###################################
        # select ongemalen incompleet spier
        ###################################
        total_spier = 0.0
        try:
            total_spier, selection = self.select_type('SPIERVLEES', order, meal_size, package_rest*0.4)
        except NoProductsException, e:
            self.exceptions.append(('SPIERVLEES', order.get_animal(), e))
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
            self.exceptions.append(('BOT', order.get_animal(), e))
            selection = []
        
        products_in_order.extend(selection)
        pkg = order.get_package()/100.0
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
