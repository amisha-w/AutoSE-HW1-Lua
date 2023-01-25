import sys
sys.path.insert(1, "../src")

from main import*
from utils import*
from num import*
from sym import*

def test_num():
    testObj = Num()
    numList = [1,1,1,1,2,2,3]
    for number in numList:
        testObj.add(number)
    return 11/7 == testObj.mid() and 0.787 == rnd(testObj.div(), 3)

def test_sym():
    testObj = Sym()
    symList = ["a","a","a","a","b","b","c"]
    for symbol in symList:
        testObj.add(symbol)
    return "a" == testObj.mid() and 1.379 == rnd(testObj.div(), 3)

def testRand():
    global seed
    testObj_1 = Num()
    testObj_2 = Num()
    for num in range(1000):
        testObj_1.add(rand(0, 1))
    seed = options['seed']
    for num in range(1000):
        testObj_2.add(rand(0, 1))
    mid_1, mid_2 = rnd(testObj_1.mid(), 1), rnd(testObj_2.mid(), 1)
    return mid_1==mid_2 and 0.5 == rnd(mid_1,1)

def testthe():
        oo(options)
        return True


if __name__ == '__main__':
    eg('the', 'show settings', testthe)
    eg('rand', 'generate, reset, regenerate same', testRand)
    eg('sym', 'check syms', test_sym)
    eg('num', 'check nums', test_num)
    main(options, help, egs)