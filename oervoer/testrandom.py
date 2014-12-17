'''
Created on Oct 14, 2014

@author: mshepher
'''
import unittest

import weighted_random
import random
import json
class Test(unittest.TestCase):


    def testRand(self):
        wr = weighted_random.WeightedRandom([random.randint(0,99) for i in xrange(20)])
        l = []
        x = []
        y = []
        for _ in range(100000):
            l.append(wr.rand())
        l.sort()
        for i in xrange(len(wr.weights)):
            x.append(l.count(i))
            y.append(x[i]/100.0)
        for i in xrange(len(x)):
            print '%-5s %10s %10s%%' % (i, wr.weights[i], y[i])

    def testJson(self):
        en = json.JSONEncoder()
        encoded = en.encode(weighted_random.WeightedRandom([random.randint(0,99) for _ in xrange(20)]))
        de = json.JSONDecoder()
        print(de.decode(encoded))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRand']
    unittest.main()