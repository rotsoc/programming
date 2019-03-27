from math import *

def Euclid(a, b):
    if a < b or b < 0:
        raise(Exception("We must have a >= b >= 0"))
    if b == 0:
        return a
    return Euclid(b, a%b)

def extended_Euclid(a, b):
    if a < b or b < 0:
        raise(Exception("We must have a >= b >= 0"))
    if b == 0:
        return (1, 0, a)
    (x, y, d) = extended_Euclid(b, a%b)
    return (y, x - floor(a/b)*y, d)

