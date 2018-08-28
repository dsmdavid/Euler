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



def createpermut(n):
    s = ""
    for x in range(1,n+1):
        s += str(x)


    listes=[]
    
    for d in itertools.permutations(s):
        listes.append(createseq(d))
    
    return listes
        
def euler40():
    l = []
    for x in range(1,10):
        lt = createpermut(x)
        for i in lt:
            try:
                l.append(int(i))
            except:
                print("x = ",x,"l = ",l)
                print(i)
                input()
                    
    return l

def isPal(string):
    return string == string[::-1]

def main():
    start = time.time()
    test = euler40()
    mn = primesfrom2to(987654321)
    m = set()
    for i in mn:
        m.add(i)


    print("starting check", time.time() -start)
    n = 0
    while n == 0:
        mv = test.pop() 
        if mv in m:
            n = 1
            print(mv)
            
        
          

    end = time.time()
    print(end-start)


main()
