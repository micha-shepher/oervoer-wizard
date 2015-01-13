'''
Created on Oct 11, 2014

@author: mshepher
'''

import csv
from operator import itemgetter
from globals import Globals

def seq(typ):
    return Globals.VLEES_TYPES.index(typ)

class Delivery(object):
    '''print and export the delivery'''
    def __init__(self, testdir, order, delivery):
        self.f = csv.writer(file('%s/%s_%s.csv' % (testdir,order.animal,order.owner),'w'))
        self.order = order
        self.delivery = delivery
        
    def bol(self, csv=False, brieven=False):
        
        total = 0.0
        picklist = ''
        if not brieven:
            picklist = 'Eigenaar: {0}, dier: {1}\n'.format(self.order.owner, self.order.animal)
        deliv = {}
        for i in self.delivery:
            if deliv.has_key(i.sku):
                deliv[i.sku][4] += 1 
            else:
                deliv[i.sku] = [seq(i.type), i.sku, i.name, i.shelf, 1, i.get_weight()]
                
        for i in sorted(deliv.items(), key=itemgetter(1)):
            a,b,c,d,e,f = i[1]
            if brieven:
                row =(Globals.VLEES_TYPES[a],c[:40],e)
                picklist += '%-20s %-40s %3s\n' % row
            else:
                row =(Globals.VLEES_TYPES[a],b,c[:40],d,e,f*1000)
                picklist += '%-20s %-20s %-40s %-15s %3s x %-10g\n' % row
            self.f.writerow(row)
            total += e*f
            
        if not brieven:
            picklist += 'Totaal pakket gewicht: {0}\n\n'.format(total) 
        return picklist
    
    def csvout(self, brieven=False):
        return self.bol(True, brieven)
