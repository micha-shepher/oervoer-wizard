'''
Created on Jan 28, 2015

@author: mshepher
'''
from wizard.models import Taste, MeatType, Product, Order, Pet, Owner
import csv
from decimal import Decimal
from wizard.brains.oervoer.oervoer import Oervoer, Delivery

class Fill(object):
    '''
    fills smaak, vleestype, product, order
    '''
    _intern = 1
    _magento = 2
    _csv = 3
    def __init__(self):
        '''
        Constructor
        '''
        
        self.smaakfile = open('/home/mshepher/Develop/oervoer-wizard/data/smaak.dat', 'r').readlines()
        self.VLEES_TYPES = ['VIS', 'VISGEMALEN', 'PENS', 'SPIER', 
                            'ZACHT BOT', 'MIDDEL BOT', 'HARD BOT', 
                            'COMPLEET KARKAS', 'COMPLEET KARKAS.ZACHT BOT', 'COMPLEET KARKAS.MIDDEL BOT', 'COMPLEET KARKAS.HARD BOT', 
                            'ORGAAN', 'GEMALEN']
        self.VLEES_DEELBAAR = ['BOT', 'ZACHT BOT', 'MIDDEL BOT', 'HARD BOT', 'GEMALEN', 'VISGEMALEN', 'ORGAAN', 'PENS', 'SPIER']
        self.KARKASSEN   = ['COMPLEET KARKAS.HARD BOT', 'COMPLEET KARKAS.MIDDEL BOT', 'COMPLEET KARKAS.ZACHT BOT', 'COMPLEET KARKAS']
        self.VISSEN      = ['VIS', 'VISGEMALEN']
        self.BOT = ['HARD BOT', 'MIDDEL BOT', 'ZACHT BOT']
        
    def fillsmaak(self): 
        Taste.objects.all().delete()
        key = ''
        for taste in self.smaakfile:
            if taste.find('key:') > -1:
                key = taste.split (':')[1].strip().upper()
            else:
                s = Taste(taste=taste.strip().upper())
                if key == 'VIS':
                    s.is_fish = True
                    if taste.find('.KOP') > -1:
                        s.is_fishhead = True
                elif key == 'GEVOGELTE':
                    s.is_fowl = True
                elif key == 'GROOTDIER':
                    s.is_big = True
                elif key == 'KLEINDIER':
                    s.is_small = True
                elif key == 'ORGAAN':
                    s.is_organ = True
                    if taste.find('.LEVER') > -1:
                        s.is_liver = True
                elif key == 'PENSBOT':
                    s.is_else = True
                s.save()
                    
    def filltype(self):
        for vtype in self.VLEES_TYPES:
            v = MeatType(meat_type=vtype)
            v.is_fish = vtype in self.VISSEN
            v.is_bot  = vtype in self.BOT
            v.is_karkas = vtype in self.KARKASSEN
            v.is_orgaan = vtype == 'ORGAAN'
            v.is_pens = vtype == 'PENS'
            v.is_spier = vtype == 'SPIER'
            v.save()
            
    def fillproduct(self):
        Product.objects.all().delete()
        products  = csv.DictReader(file('/home/mshepher/Develop/oervoer-wizard/test/products.csv',  'r'))
        for prod in products:
            if prod['geschiktmenu'].upper() == 'NEE' or\
               prod['is_in_stock'] == '0':
                continue
            p = Product()
            print prod.values()
            p.name = prod['name']
            p.sku  = prod['sku']
            p.qty  = prod['qty']
            
            print prod['smaak'].strip().upper()
            smaak = Taste.objects.get(taste=prod['smaak'].strip().upper())
            
            p.smaak = smaak
            
            vlees = MeatType.objects.get(meat_type=prod['type_vlees'].strip().upper())
            p.vlees = vlees
            p.shelf = prod['shelf'].strip().upper()
            p.weight = Decimal(prod['weight'])
            p.verpakking = prod['verpakt_per']
            kat_hond = prod['geschikt voor'].strip().upper()
            if 'KAT' in kat_hond and 'HOND' in kat_hond:
                p.kat_hond = 'Beide'
            elif 'KAT' in kat_hond:
                p.kat_hond = 'KAT'
            elif 'HOND' in kat_hond:
                p.kat_hond = 'HOND'
            else:
                p.kat_hond = 'Beide'
            p.save() 
            
            
            
class testOervoer(object):
    def __init__(self):
        self.oer = Oervoer(None,None,None)
        self.oer.parse_products()
        print len(self.oer.products)
        print len(self.oer.ordlist)
        for i in range(5):
            result = self.oer.process_order(self.oer.ordlist[i])
            d = Delivery('', self.oer.ordlist[i], result)
            print d.bol()

        
if __name__ == '__main__':
    import django
    django.setup()
    #c = Fill()
    #c.fillsmaak()
    #c.fillproduct()
    
    o = testOervoer()
    