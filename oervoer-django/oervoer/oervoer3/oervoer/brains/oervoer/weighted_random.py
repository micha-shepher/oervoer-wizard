'''
Created on Oct 14, 2014

@author: mshepher
'''

import random

from ... import logger


class WeightedRandom(object):
    '''
    classdocs
    '''

    def __init__(self, weights):
        '''
        Constructor
        '''
        self.weights = weights
        self.sum = [0]
        sig = 0
        for i in range(len(weights)):
            sig += weights[i]
            self.sum.append(sig)

    def rand(self):
        try:
            r = random.randint(0, self.sum[-1])
            i = 0
            while r > self.sum[i]:
                i += 1
        except:
            logger.error('rand functie fail {0}, lege lijst!'.format(self.sum))
            raise ValueError('empty list')
        return i - 1
