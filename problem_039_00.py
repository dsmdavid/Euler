##Take the number 192 and multiply it by each of 1, 2, and 3:
##
##192 × 1 = 192
##192 × 2 = 384
##192 × 3 = 576
##By concatenating each product we get the 1 to 9 pandigital,
##192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
##
##The same can be achieved by starting with 9 and multiplying by
##1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the
##concatenated product of 9 and (1,2,3,4,5).
##
##What is the largest 1 to 9 pandigital 9-digit number that can be formed
##as the concatenated product of an integer with (1,2, ... , n) where n > 1?

# find the list of pandigital numbers.
# sort the list.
# test for concatenated product.

import numpy as np
import itertools
import math
import time

def createseq(tupleseq):
    seq = ""
    for i in tupleseq:
        seq += i
    return seq    

def pandigital(n1,n2,n3, N):
    seq = set(str(n1)+str(n2)+str(n3))
    if "0" in seq: return False
    if len(seq) != N: return False
    return True

    
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    for i in range(1,int((n**0.5)/3+1)):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]


def isTriangle(n1,n2, N):
    n3 = N-n1-n2
    if n1 == n2 or n1 == n3 or n2 == n3:
        return False
    if n1**2 + n2**2 - n3**2 != 0:
        return False
    else:
        return True

def solutions(N):
    solutions = set()
    for i in range(1,int(N/2)):
        for j in range(i+1,int(N/2)):
            if isTriangle(i,j,N):
                l =[]
                l.append(i)
                l.append(j)
                l.sort()
                
                
                
                solutions.add((l[0],l[1]))
##    print(solutions)
    return N, len(solutions)
    
        
def euler39():
    dicts = {}
    maxv = 0
    for n in range(1,10011):
        a,b = solutions(n)
        dicts[b] = a
        maxv = max(maxv,b)
##    print(dicts)
    print(maxv, dicts[maxv])
        

                
            
    
   

def main():
    start = time.time()
    m = euler39()

    end = time.time()
    print(end-start)


main()
