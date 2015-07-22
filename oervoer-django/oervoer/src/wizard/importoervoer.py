'''utility to import Magento stuff into wizard.'''

import pymysql
import phpserialize
import re
import string
import pprint
from wizard.models import Taste, MeatType, Product

def override(f):
    return f

class ImportOervoer(object):
    '''connect to the oervoer mysql server and import the stuff we need for the wizard.
    these are: orders, products, owners, pets, tastes and meattypes.
    owners and pets are gathered from the order table.'''
    
    def __init__(self, user, pw, cur=None):
        self.user = user
        self.pw = pw
        self.cur = cur
        self.conn = None
        
        if not cur:
            self.connect()
    
    def connect(self):
        if self.conn:
            return True
        try:
            print 'connecting to {}@{}'.format(self.user, 'oervoer.com')
            self.conn = pymysql.connect(host='oervoer.com', port=3306,
                                        user=self.user, passwd=self.pw, db='bvdheide_magento')
            print 'connected'
        except pymysql.err.OperationalError:
            print 'no connection'
            return False

    def execute(self):
        try:
            self.cur = self.conn.cursor()
            self.cur.execute(self.query)
            return True
        except pymysql.err.OperationalError:
            print 'cannot obtain cursor'
            return False

    def get_cur(self):
        return self.cur

    def set_query(self, query):
        self.query = query
            
    def importtable(self):
        
        self.execute()
        query_results = self.cur.fetchall()
        return query_results

class ImportProds(ImportOervoer):
    
    @override
    def importtable(self):
        #{'id','name','sku','qty','smaak','vlees','shelf','weight', 'verpakking', kat_hond})
        query = '''
        SELECT DISTINCT p.entity_id, p.name, p.sku, inv.qty, eav.value, eav2.value, p.shelf, p.weight, p.verpakt_per, p.geschikt
        FROM  `catalog_product_flat_1` AS p
        INNER JOIN cataloginventory_stock_item AS inv
        ON inv.product_id = p.entity_id
        JOIN eav_attribute_option_value AS eav
        ON eav.option_id=p.smaak
        JOIN eav_attribute_option_value AS eav2
        ON eav2.option_id=p.type_vlees
        
        WHERE p.geschiktmenu =1 AND inv.is_in_stock = 1 AND eav.store_id=0
        '''
        self.set_query(query)
        self.results = [list(i) for i in super(ImportProds, self).importtable()]
        query3 = '''SELECT DISTINCT option_id, value FROM eav_attribute_option_value AS eav 
                    WHERE eav.option_id in (135,136,137,138,147,148) AND
                          eav.store_id=0'''
        self.set_query(query3)
        if self.execute():
            cat_dog = dict(self.cur.fetchall())

        for prod in self.results:
            kat = False
            hond = False
            try:
                geschikt = [int(i) for i in prod[-1].split(',')]
                print prod[2], geschikt
                for ind in geschikt:
                
                    ind = int(ind)
                    if cat_dog.has_key(ind):    
                        kat = kat or 'KAT' in cat_dog[ind].upper()
                        hond = hond or 'HOND' in cat_dog[ind].upper()
                    else:
                        print 'no key {}'.format(ind)
            except ValueError:
                pass
            prod[-1] = (hond,kat,)
        return self.processresults()
            
    def processresults(self):
        adjusted = []
        #{'id','name','sku','qty','smaak','vlees','shelf','weight', 'verpakking', kat_hond})
        for rec in self.results:
            if rec[3] == '0':
                print 'discarded geen voorraad {}'.format(rec[2])
                continue
            try:
                smaak = Taste.objects.get(taste=rec[4].strip().upper())
            except Taste.DoesNotExist:
                print 'discarded geen smaak {} {}'.format(rec[2], rec[4])
                continue # dont bother with this product
            try:
                vlees = MeatType.objects.get(meat_type=rec[5].strip().upper())
            except MeatType.DoesNotExist:
                print 'discarded geen vlees type {} {}'.format(rec[2], rec[5])
                continue
            hond, kat = rec[9]
            if rec[6] is None:
                rec[6] = 'MYSTERIE'
            if kat:
                if hond:
                    rec[9] = Product.KATHOND[-1][0]
                else:
                    rec[9] = Product.KATHOND[0][0]
            else:
                if hond:
                    rec[9] = Product.KATHOND[1][0]
                else:
                    print 'strange product niet geschikt noch kat noch hond {}'.format(rec[2])
                    continue
            adjusted.append({'id': rec[0], 'name': rec[1], 'sku': rec[2],
                 'qty': rec[3],'smaak':smaak, 'vlees':vlees, 'shelf':rec[6],
                 'weight':rec[7], 'verpakking':rec[8], 'kat_hond':rec[9]})

        return adjusted
    
class ImportOrders(ImportOervoer):
    
    def get_name_and_weight(self, options):
        name = 'niet bekend'
        weight = '10'
        pat = re.compile('(\d+\.{0,1}\d*)')
    
        for option in options.keys():
            
            if options[option]['label'].find('Wat is de naam') > -1:
                name = options[option]['option_value']
            if options[option]['label'].find('Wat is het gewicht') > -1:
                weight = options[option]['option_value']
                weight = weight.replace(',','.')
                m = re.search(pat, weight)
                if m:
                    weight = m.group(0)
                
        return name, weight
 
    def lengthreplace(self, matchobj):
        '''replace badly generated string length to fix PHP serialize bug.
        '''   
        a = matchobj.group(1)
        b = matchobj.group(2)
        if not int(a) == len(b):
            return 's:{}:"{}"'.format(len(b),b)
        else:
            return matchobj.group(0)
     
    def correct_string_len(self, s):
        '''example: "s:17:bla bla bla bla bla b"
                     matches. group 1 is '17' and group 2 is "bla bla bla bla bla b" '''
        pat = re.compile(r's:(\d*?):"(.*?)"')
        return re.sub(pat, self.lengthreplace, s)
    
    @override
    def importtable(self):
        query ='''
        SELECT item.item_id, sal.entity_id, sal.status, sal.customer_id, sal.customer_firstname, sal.customer_lastname, item.product_id, item.weight, item.qty_ordered, item.product_options
        FROM  `sales_flat_order` AS sal
        INNER JOIN sales_flat_order_item AS item
        ON sal.entity_id=item.order_id
        WHERE sal.status in ('processing','pending') AND item.product_id in (58,60,85,125,126,127,187,192,193,423,424,425,426,427,428)
        '''
        self.set_query(query)
    
        results = [list(i) for i in super(ImportOrders, self).importtable()]
        return self.processResults(results)

    def importallorders(self):
        #      0              1           2                3                       4                      5                6            7(=-1)  
        query ='''
        SELECT item.item_id, sal.entity_id, item.order_id, sal.status, sal.customer_id, sal.customer_firstname, sal.customer_lastname, item.product_id, item.weight, item.qty_ordered, item.product_options
        FROM  `sales_flat_order` AS sal
        INNER JOIN sales_flat_order_item AS item
        ON sal.entity_id=item.order_id
        WHERE item.product_id in (58,60,85,125,126,127,187,192,193,423,424,425,426,427,428)
        '''
        self.set_query(query)
    
        results = [list(i) for i in super(ImportOrders, self).importtable()]
        return self.processResults(results)
                
    def processResults(self, results):
        adjusted_results = []
        for r in results:
            pakket = r[6] # actually product_id
            if pakket in (58,125,193,425,426):   # hard coded
                pak = 'PLUS'
            elif pakket in (85,126,187,427,428):
                pak = 'COMBI'
            else:
                pak = '100'
            if pakket in (58,60,85,187,192,193): # hard coded(!)
                kh = 'HOND'
            else:
                kh = 'KAT'
        
            s=filter(lambda x: x in string.printable, r[-1]) # last field is options field, where the owner,
                                                             # pet name and weight are stored.
            try:
                d = phpserialize.loads(self.correct_string_len(s))    # this string (s) is already without strange characters
            except ValueError:
                d={}
                print 'bad options voor {}'.format(str(r[-1]))

            weight=10
            name='onbekend'
            if d.has_key('options'):
                name, weight = self.get_name_and_weight(d['options'])
            else:

                print r[0],r[1],r[7],' does not have options!'
                print d.keys()
            # .......      order_id | sts | custid | customer name |  pakket | kat/hond | gewicht pak | pet | gewicht pet
            adjusted_results.append({'id':r[0],'status':r[2],'customer_id':r[3],'customer_name':' '.join((r[4], r[5])),
                              'pakket':pak, 'ras':kh, 'gewicht_pak': float(r[7]*r[8]), 'name':name, 'weight':weight, 'item_id':r[1]})
            #adjusted_results[r[0]] = r[1], r[2], ' '.join((r[3], r[4])), pak, kh,      r[6],         name, weight
        
        return adjusted_results
    
    
class ImportSmaak(ImportOervoer):
    
    @override
    def importtable(self):
        query ='''
        SELECT DISTINCT v.option_id, v.value
        FROM  eav_attribute_option AS o
        INNER JOIN eav_attribute_option_value AS v ON o.option_id = v.option_id
        WHERE (o.attribute_id =183) AND (v.store_id = 0)
        ORDER BY v.value
        '''
        self.set_query(query)
        return dict(super(ImportSmaak, self).importtable())

        #query2='''
        #SELECT * FROM smaken WHERE 1'''
    
class ImportVlees(ImportOervoer):
    
    @override
    def importtable(self):
        query ='''
        SELECT DISTINCT v.option_id, v.value 
        FROM  eav_attribute_option AS o
        INNER JOIN eav_attribute_option_value AS v ON o.option_id = v.option_id
        WHERE o.attribute_id =184
        ORDER BY v.value
        '''
        self.set_query(query)
        return dict(super(ImportVlees, self).importtable())
        
    
if __name__ == '__main__':
    user = 'bvdheide_micha'
    pw = 'lelijkgedrocht'
    
    imp = ImportOrders(user, pw)
    if imp.connect():
        savecur = imp.get_cur()
    imp.importtable()
    
    imp = ImportProds(user, pw, savecur)
    pprint.pprint( imp.importtable())

    imp = ImportSmaak(user, pw, savecur)
    imp.importtable()
    
        
    imp = ImportVlees(user, pw, savecur)
    imp.importtable()
    

    
    
