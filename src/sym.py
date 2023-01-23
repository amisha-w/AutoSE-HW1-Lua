import math

class Sym:
    def __init__(self):
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None
    

    def add(self, x: str):
        '''
        Adds count for x
        '''
        if x != "?":
            self.n += 1
            if x in self.has:
                self.has[x] = self.has[x] + 1
            else:
                self.has[x] = 1

            if self.has[x] > self.most:
                self.most = self.has[x]
                self.mode = x  
    
    
    def mid(self):
        '''
        Returns mode 
        '''
        return self.mode


    def div(self):
        '''
        Returns the standard deviation
        '''
        def FUN(p):
            return p * math.log(p, 2)

        e = 0
        for key,val in self.has.items():
            e += FUN(val/self.n)

        return -e