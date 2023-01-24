from src.sym import Sym
from src.utils import *

def test_sym():
    testObj = Sym()
    symList = ["a","a","a","a","b","b","c"]
    for symbol in symList:
        testObj.add(symbol)
    return "a" == testObj.mid() and 1.379 == rnd(testObj.div(), 3)

test_sym()