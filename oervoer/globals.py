'''
Created on Oct 11, 2014

@author: mshepher
'''
import re

class Globals(object):
    MEALFACTOR  = 4  # included products that are bigger than meal size by this factor
    MEALFACTOR2 = 0.20# included products smaller than meal size by this factor
    pat         = re.compile('(.*?),')
    CATFACTOR   = 0.035 # 35 gram / kg / day
    DOGFACTOR   = 0.025 # 25 gram / kg / day
    FACTOR      = {'KAT':CATFACTOR, 'HOND':DOGFACTOR}
    tries       = 10
    VIS         = 'VIS'
    PENS        = 'PENS'
    ORGAAN      = 'ORGAAN'
    SPIER       = 'SPIERVLEES'
    ZACHTBOT    = 'ZACHT BOT'
    HARDBOT     = 'HARD BOT'
    GEMALEN     = 'COMPLETE GEMALEN'
    KARKAS      = 'COMPLEET KARKAS'
    BOT         = 'BOT'
    VLEES_TYPES = [VIS, PENS, SPIER, ZACHTBOT, HARDBOT, KARKAS, ORGAAN, GEMALEN]
    TESTENV     = 'OERVOERTESTENV'
