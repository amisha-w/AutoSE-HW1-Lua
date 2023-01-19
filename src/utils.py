import math


seed = 937162211
def rand(low, high):

    global  seed
    if low is None:
        low = 0
    if high is None:
        high = 1
    seed = (16807 * seed) % 2147483647
    return low + (high -low) * seed / 2147483647

def rint(low, high):
    return math.floor(0.5 + rand(low, high))

def rnd(n, n_places):
    if not n_places:
        n_places = 3
    mult = math.pow(10, n_places)
    return math.floor(n * mult * 0.5)/mult

def map(t, fun):





