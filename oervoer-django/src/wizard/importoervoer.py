
import pymysql
import phpserialize
import re
import string
import pprint


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
        query = '''
        SELECT DISTINCT inv.qty, p.weight, p.sku, p.name, eav.value, eav2.value, p.verpakt_per, p.geschikt
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
        results = [list(i) for i in super(ImportProds, self).importtable()]
        query3 = '''SELECT DISTINCT option_id, value FROM eav_attribute_option_value AS eav 
                    WHERE eav.option_id in (136,137,138) AND
                          eav.store_id=0'''
        self.set_query(query3)
        if self.execute():
            cat_dog = dict(self.cur.fetchall())
            print cat_dog
        for prod in results:
            kat = False
            hond = False
            try:
                geschikt = [int(i) for i in prod[-1].split(',')]
                for ind in geschikt:
                
                    ind = int(ind)
                    if cat_dog.has_key(ind):    
                        kat = kat or 'Kat' in cat_dog[ind]
                        hond = hond or 'Hond' in cat_dog[ind]
                    else:
                        print 'no key {}'.format(ind)
            except ValueError:
                pass
            prod[-1] = (hond,kat,)
        return results
            
        
              
    
class ImportOrders(ImportOervoer):
    
    def get_name_and_weight(self, options):
        name = 'niet bekend'
        weight = '10'
        pat = re.compile('(\d+\.{0,1}\d*)')
    
        for option in options.keys():
            
            if options[option]['label'].startswith('Wat is de naam'):
                name = options[option]['option_value']
            if options[option]['label'].startswith('Wat is het gewicht'):
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
        SELECT sal.entity_id, sal.status, sal.customer_id, sal.customer_firstname, sal.customer_lastname, item.product_id, item.weight, item.product_options
        FROM  `sales_flat_order` AS sal
        INNER JOIN sales_flat_order_item AS item
        ON sal.entity_id=item.order_id
        WHERE sal.status in ('processing','pending') AND item.product_id in (58,60,85,125,126,127)
        '''
        self.set_query(query)
    
        results = [list(i) for i in super(ImportOrders, self).importtable()]
        return self.processResults(results)

    def importallorders(self):
        #      0              1           2                3                       4                      5                6            7(=-1)  
        query ='''
        SELECT item.order_id, sal.status, sal.customer_id, sal.customer_firstname, sal.customer_lastname, item.product_id, item.weight, item.product_options
        FROM  `sales_flat_order` AS sal
        INNER JOIN sales_flat_order_item AS item
        ON sal.entity_id=item.order_id
        WHERE item.product_id in (58,60,85,125,126,127)
        '''
        self.set_query(query)
    
        results = [list(i) for i in super(ImportOrders, self).importtable()]
        return self.processResults(results)
                
    def processResults(self, results):
        adjusted_results = []
        for r in results:
            pakket = r[5] # actually product_id
            if pakket in (58,125):   # hard coded
                pak = 'PLUS'
            elif pakket in (85,126):
                pak = 'COMBI'
            else:
                pak = '100'
            if pakket in (58,60,85): # hard coded(!)
                kh = 'HOND'
            else:
                kh = 'KAT'
            r[5] = pak
        
            s=filter(lambda x: x in string.printable, r[-1]) # last field is options field, where the owner, 
                                                             # pet name and weight are stored.
            try:
                d = phpserialize.loads(self.correct_string_len(s))    # this string (s) is already without strange characters
            except ValueError:
                d={}
                print 'bad options voor {}'.format(str(r[:-1]))
    #    pprint.pprint (d)
            weight=10
            name='onbekend'
            if d.has_key('options'):
                name, weight = self.get_name_and_weight(d['options'])
            # .......      order_id | sts | custid | customer name |  pakket | kat/hond | gewicht pak | pet | gewicht pet
            adjusted_results.append({'id':r[0],'status':r[1],'customer_id':r[2],'customer_name':' '.join((r[3], r[4])),
                              'pakket':pak, 'ras':kh, 'gewicht_pak': r[6], 'name':name, 'weight':weight})
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
    

    
    
