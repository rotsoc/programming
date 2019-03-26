from math import *

def multiply(x,y):
    if y < 0:
        raise(Exception("The second argument has to be non-negative"))
    if y == 0:
        return 0
    z = multiply(x,floor(y/2))
    if y%2 == 0:
        return 2*z
    else:
        return x + 2*z

