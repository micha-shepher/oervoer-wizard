'''
Created on Apr 14, 2015

@author: mshepher
'''
from django.test import TestCase
from wizard.brains.oervoer.oervoer import Oervoer

class OervoerTest(TestCase):


    def testLoad(self):
        oer = Oervoer(None,None,None)
        oer.parse_products()
        assert(len(oer.prodlists)>0)
        assert(len(oer.ordlist)>0)
        oer.process_order(oer.ordlist[0])

