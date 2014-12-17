'''
Created on Oct 11, 2014

@author: mshepher
'''

from globals import Globals

class Product(object):
    STORE = 0
    SKU = 1
    QTY = 2 # int
    IS_IN_STOCK = 3
    GESCHIKT_MENU = 4
    NAME = 5
    SMAAK = 6
    TYP_VLEES = 7
    SHELF = 8
    WEIGHT = 9  #float
    VERPAKKING = 10
    
    def __init__(self, product):
        '''product in inventory'''
        rec = product.strip().split(',')
        self.sku = rec[self.SKU]
        try:
            self.qty = int(float(rec[self.QTY]))
        except ValueError:
            print 'produkt %s heeft geen vooraad.' % rec[self.NAME]
            self.qty = 0
        self.name = rec[self.NAME]
        self.include = rec[self.GESCHIKT_MENU] == 'Ja'
        self.smaak = rec[self.SMAAK].upper()
        self.type = rec[self.TYP_VLEES].upper()
        self.shelf = rec[self.SHELF]
        try:
            self.verpakking = int(rec[self.VERPAKKING])
        except ValueError:
            print 'produkt heeft een nonnumerische verpakking eenheid %s' % self.name
            self.verpakking = 1
        try:
            self.weight = float(rec[self.WEIGHT])
        except ValueError:
            self.weight = 0.0
            print 'produkt %s heeft geen gewicht.' % self.name
            
    def get_type(self):
        return self.type
 
    def get_include(self):
        return self.include

    def get_qty(self):
        return self.qty
    
    def get_weight(self):
        return self.weight
    
    def get_norm_weight(self):
        return self.weight/self.verpakking
    
    def dump(self):
        print '%s, type %s qty %s, weight %s, smaak %s' % (self.name, self.get_type(), self.get_qty(), self.weight, self.smaak)
