##The number 3797 has an interesting property.
##Being prime itself, it is possible to continuously
##remove digits from left to right, and remain prime at each stage:
##    3797, 797, 97, and 7. Similarly we can work from right to left:
##        3797, 379, 37, and 3.
##
##Find the sum of the only eleven primes that are both truncatable
##from left to right and right to left.
##
##NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import numpy as np
import time
import math
import time

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    for i in range(1,int((n**0.5)/3+1)):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

def truncl(n,listprime):
    if len(str(n)) == 1:
        return n in listprime
    else:
        if n in listprime:
            return truncl(int(str(n)[1::]),listprime)
def truncr(n,listprime):
    if len(str(n)) == 1:
        return n in listprime
    else:
        if n in listprime:
            return truncr(int(str(n)[:len(str(n))-1:]),listprime)

def truncatable(n,listprime):
    if n == 2 or n==3 or n==5 or n ==7:
        return False
    if truncl(n,listprime):
        if truncr(n,listprime):
            return True
        
def euler37(Nmax):
    # primes from 1, 1000000?
    n = []
    lp = primesfrom2to(Nmax)
    for i in lp:
        if truncatable(i,lp):
            n.append(i)
            if len(n) == 11:
                return n
    return n

def isPal(string):
    return string == string[::-1]
##        return True
##    else:
##        return False

def main():
    start = time.time()
##    print(truncl(3797,
    m = euler37(1000000)
    d = sum(m)
    print(d)
    print(m)
##    print(truncatable(3796,primesfrom2to(3798)))
##    print(n)
    end = time.time()
    print(end-start)


main()
