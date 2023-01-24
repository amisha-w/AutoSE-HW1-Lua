from src.num import NUM
from src.utils import *

def test_num():
    testObj = NUM()
    numList = [1,1,1,1,2,2,3]
    for number in numList:
        testObj.add(number)
    assert 11/7 == testObj.mid()
    assert 0.787 == rnd(testObj.div(), 3)

test_num()