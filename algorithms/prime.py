from math import *
from secrets import randbelow

def primality(N):
    a = randbelow(N)
    if (a**(N-1))%N == 1:
        return True
    else:
        return False

def primality2(N):
    A = [randbelow(N) for i in range(10)]
    res = True
    for i in range(10):
        if (A[i]**(N-1))%N == 1:
            continue
        else:
            return False
    return res
            
            
