from math import *

def modexp(x, y, N):
    if type(y) != int:
        raise(Exception("The second argument [the exponent] has to be integer"))
    if y == 0:
        return 1
    z = modexp(x, floor(y/2), N)
    if y%2 == 0:
        return (z**2)%N
    else:
        return (x*(z**2))%N
