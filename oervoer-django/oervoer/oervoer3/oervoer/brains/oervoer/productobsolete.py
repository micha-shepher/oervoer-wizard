'''
Created on Oct 11, 2014

@author: mshepher
'''

from globals import Globals

class Product(object):
    SKU = 'sku'
    QTY = 'qty'
    IS_IN_STOCK = 'is_in_stock'
    GESCHIKT_MENU = 'geschiktmenu'
    NAME = 'name'
    SMAAK = 'smaak'
    TYP_VLEES = 'type_vlees'
    SHELF = 'shelf'
    WEIGHT = 'weight'  #float
    VERPAKKING = 'verpakt_per'
    KAT_HOND = 'geschikt voor'
    
    def __init__(self, prod):
        '''product in inventory'''
        #prod = product.strip().split(',')
        self.sku = prod[self.SKU]
        try:
            self.qty = int(float(prod[self.QTY]))
        except ValueError:
            print 'produkt %s heeft geen vooraad.' % prod[self.NAME]
            self.qty = 0
        self.name = prod[self.NAME]
        self.include = prod[self.GESCHIKT_MENU].upper() == 'JA'
        self.smaak = prod[self.SMAAK].upper()
        self.type = prod[self.TYP_VLEES].upper()
        self.shelf = prod[self.SHELF]
        try:
            self.verpakking = int(prod[self.VERPAKKING])
        except ValueError:
            print 'produkt heeft een nonnumerische verpakking eenheid %s' % self.name
            self.verpakking = 1
        try:
            self.weight = float(prod[self.WEIGHT])
        except ValueError:
            self.weight = 0.0
            print 'produkt %s heeft geen gewicht.' % self.name
        try:
            x = prod[self.KAT_HOND].upper()
            self.kathond = {'KAT':'KAT' in x, 'HOND':'HOND' in x}
        except KeyError:
            self.kathond = {'KAT':True, 'HOND':True}
                
    def get_kathond(self, kathond):
        return self.kathond[kathond]

    def get_type(self):
        return self.type
 
    def get_include(self):
        return self.include

    def get_qty(self):
        return self.qty
    
    def get_weight(self):
        return self.weight
    
    def get_norm_weight(self):
        if self.verpakking == 0:
            self.verpakking = 1
        return self.weight/self.verpakking
    
    def dump(self):
        print 'type %s, name %s qty %s, weight %s, smaak %s' % (self.get_type(), self.sku, self.get_qty(), self.weight, self.smaak)
