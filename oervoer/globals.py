'''
Created on Oct 11, 2014

@author: mshepher
'''
import re

class Globals(object):
    MEALFACTOR  = 4  # included products that are bigger than meal size by this factor
    MEALFACTOR2 = 0.20# included products smaller than meal size by this factor
    MEALFACTOR3 = 1.5
    pat         = re.compile('(.*?),')
    CATFACTOR   = 0.035 # 35 gram / kg / day
    DOGFACTOR   = 0.025 # 25 gram / kg / day
    FACTOR      = {'KAT':CATFACTOR, 'HOND':DOGFACTOR}
    tries       = 10
    LIKEFACTOR  = 4.0 # sets the selection likelihood to be times this factor.
    VIS         = 'VIS'
    PENS        = 'PENS'
    ORGAAN      = 'ORGAAN'
    SPIER       = 'SPIERVLEES'
    ZACHTBOT    = 'ZACHT BOT'
    MIDDELBOT   = 'MIDDEL BOT'
    HARDBOT     = 'HARD BOT'
    GEMALEN     = 'COMPLEET GEMALEN'
    KARKAS      = 'COMPLEET KARKAS'
    BOT         = 'BOT'
    LEVER       = 'LEVER'
    VISGEMALEN  = 'GEMALEN VIS'
    HEAD        = 'KOP'
    SMALLMEAL   = 250
    BIGMEAL     = 500
    VLEES_TYPES = [VIS, VISGEMALEN, PENS, SPIER, ZACHTBOT, MIDDELBOT, HARDBOT, KARKAS, ORGAAN, GEMALEN]
    VLEES_DEELBAAR = [GEMALEN, VISGEMALEN, ORGAAN, PENS, SPIER]
    TESTENV     = 'OERVOERTESTENV'
