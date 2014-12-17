'''
Created on Oct 14, 2014

@author: mshepher
'''

import random
class WeightedRandom(object):
    '''
    classdocs
    '''

    def __init__(self, weights):
        '''
        Constructor
        '''
        self.weights = weights
        self.sum = []
        sig = 0
        for i in xrange(0, len(weights)):
            sig += weights[i]
            self.sum.append(sig)
        #self.sum.append(20*sig)
        
    def rand(self):
        r = random.randint(0, self.sum[-1])
        i = 0
        while r > self.sum[i]:
            i += 1
        return i
        