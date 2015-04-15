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
        
        profile = self.order.pet.profile
        deliv = {}
        for i in self.delivery:
            if deliv.has_key(i.sku):
                deliv[i.sku]['aantal'] += 1 
            else:
                deliv[i.sku] = {'vleestype':i.vlees, 'sku':i.sku, 'name':i.name, 'shelf': i.shelf, 'aantal':1, 'gram':i.weight*1000}
        #vleestype = tables.Column()
        #sku = tables.Column()
        #name = tables.Column()
        #shelf = tables.Column()
        #aantal = tables.Column()
        #x = tables.Column()
        #gram = tables.Column()
        tab = deliv.values()
        tab = sorted(tab, key=itemgetter('sku'))
        
        table = PickListTable(tab)
        return table
    

