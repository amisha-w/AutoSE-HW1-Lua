from src.num import NUM
from src.utils import *


class RandTest:

    def __init__(self, seed):
        self.tempSeed = seed
        self.seed = seed

    def testRand(self):
        testObj_1 = NUM()
        testObj_2 = NUM()
        for num in range(1000):
            testObj_1.add(self.rand(0, 1))
        self.seed = self.tempSeed
        for num in range(1000):
            testObj_2.add(self.rand(0, 1))
        mid_1, mid_2 = rnd(testObj_1.mid(), 10), rnd(testObj_2.mid(), 10)
        return mid_1==mid_2 and 0.5 == rnd(mid_1,1)

    def rand(self, lo, hi):
        lo = lo or 0
        hi = hi or 1
        self.seed = ((16807 * self.seed) % 2147483647)
        return lo + (hi - lo) * self.seed / 2147483647

