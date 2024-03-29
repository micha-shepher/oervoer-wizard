'''
Created on Oct 11, 2014

@author: mshepher
'''

from globals import Globals

class Order(object):
    EIGENAAR = 0
    DIER = 1
    GESLACHT = 2
    GECASTREERD = 3
    AKTIEF = 4
    OVERGANGS = 5
    GEWICHT = 6  #numerical
    PAKKETKG = 7 #float
    SOORT = 8
    PUP = 9
    RAS = 10

    def __init__(self,order):
        '''order = line from csv file, unparsed'''
        rec = order.strip().split(',')
        self.base = rec[:self.RAS+1]
        self.owner, self.animal = rec[:self.GESLACHT]
        self.weight = float(rec[self.GEWICHT])
        self.package = float(rec[self.PAKKETKG])
        self.kind = rec[self.SOORT].upper()
        self.ras  = rec[self.RAS].upper()
        rest = rec[self.RAS+1:]
        if '|' in rest:
            splitter = rest.index('|')
            self.donts = [i.upper() for i in rest[:splitter]]
            self.prefers = [i.upper() for i in rest[splitter+1:]]
        else:
            self.donts = [i.upper() for i in rest]
            self.prefers = []
        self.factor = 1.0
        self.result = None
        self.portie = 'beide'

    def get_prefers(self):
        return self.prefers

    def set_prefers(self, value):
        self.prefers = value

    def get_base(self):
        return ','.join(self.base)
    
    def is_allergic(self,stuff):
        '''true if animal is allergic to stuff'''
        return stuff in self.donts
    
    def get_donts(self):
        return self.donts
    
    def set_donts(self, donts):
        self.donts = donts

    def get_days(self):
        return round(self.package / (self.weight * Globals.FACTOR[self.ras]))

    def get_meal_size(self):        
        return self.weight * self.factor * Globals.FACTOR[self.ras] / 2
    
    def get_weight(self):
        return self.weight
    
    def get_package(self):
        return self.package

    def get_kind(self):
        return self.kind
    
    def get_owner(self):
        return self.owner
    
    def get_animal(self):
        return self.animal
    
    def get_ras(self):
        return self.ras

    def set_result(self, result):
        self.result = result
    
    def get_result(self):
        return self.result

    def get_factor(self):
        return self.factor
    
    def set_factor(self, factor):
        self.factor = factor
        
    def get_portie(self):
        return self.portie
    
    def set_portie(self, portie):
        self.portie = portie