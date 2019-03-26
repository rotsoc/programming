from math import *

def divide(x, y):
    if y < 1:
        raise(Exception("The second argument must be larger than 1"))
    if x == 0:
        (q, r) = (0, 0)
        return (q, r)
    (q, r) = divide(floor(x/2), y)
    q = 2*q
    r = 2*r
    if x%2 == 1:
        r += 1
    if r >= y:
        r = r - y
        q += 1
    return (q, r)
