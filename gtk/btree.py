import random
class btree(object):
    def __init__(self, value, median=477):
        self.value = value
        self.left = None
        self.right = None
        self.median = median

    def insert(self, val):
        if val < self.value:
            if not self.left:
                self.left = btree(val, self.median)
            else:
                self.left.insert(val)
        elif val > self.value:
            if not self.right:
                self.right = btree(val, self.median)
            else:
                self.right.insert(val)
        else:
            pass

    def remove(self, val):
        if val < self.value:
            if not self.left:
                return
            else:
                if self.left.value == val:
                    if self.left.left and self.left.right:
                        pass
                else:
                    self.left.remove(val)
        elif val > self.value:
            if not self.right:
                return
            else:
                self.right.remove(val)
        else:
            pass

    def traverse(self,l):
        if self.left:
            self.left.traverse(l)
        l.append(self.value)
        if self.right:
            self.right.traverse(l)
        return l
        
        
    def dump(self):
        if self.left:
            self.left.dump()
        print self.value,
        
        if self.right:
            self.right.dump()
        
if __name__ == '__main__':
    b = btree(600)
    for i in xrange(50):
        b.insert(random.randint(-1000, 1000))

    outlist = []
    print b.traverse(outlist)
    b.dump()
