'''
Created on Oct 11, 2014

@author: mshepher
'''

import csv
from operator import itemgetter
from wizard.tables import PickListTable

class Delivery(object):
    '''print and export the delivery'''
    def __init__(self, testdir, order, delivery):
        self.order = order
        self.delivery = delivery
        
    def bol(self, csv=False, brieven=False):
        
        def seq(vleestype):
            return ['VIS', 'GEMALEN VIS', 'PENS', 'SPIERVLEES', 'ZACHT BOT', 
                    'MIDDEL BOT', 'HARD BOT',
                    'COMPLEET KARKAS', 'COMPLEET KARKAS.ZACHT BOT', 'COMPLEET KARKAS.MIDDEL BOT', 'COMPLEET KARKAS.HARD BOT',
                    'ORGAAN', 'COMPLEET GEMALEN'].index(vleestype)
                    
        profile = self.order.pet.profile
        deliv = {}
        for i in self.delivery:
            if deliv.has_key(i.sku):
                deliv[i.sku]['aantal'] += 1 
            else:
                deliv[i.sku] = {'seq': seq(i.vlees.meat_type), 'vleestype':i.vlees, 'sku':i.sku, 'name':i.name, 'shelf': i.shelf, 'aantal':1, 'gram':i.weight*1000}
        #vleestype = tables.Column()
        #sku = tables.Column()
        #name = tables.Column()
        #shelf = tables.Column()
        #aantal = tables.Column()
        #gram = tables.Column()
        tab = deliv.values()
        tab = sorted(tab, key=itemgetter('seq'))
        for i in tab:
            i.pop('seq')
        
        table = PickListTable(tab)
        return table
    

