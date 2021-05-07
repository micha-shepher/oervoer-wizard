'''
Created on Apr 15, 2015

@author: mshepher
'''

class OervoerException(Exception):
    '''
    classdocs
    '''


    def __init__(self, description):
        '''
        Constructor
        '''
        self.description = description
    
    def __str__(self):
        return self.description
                