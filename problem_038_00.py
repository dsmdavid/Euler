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


        
def euler38():
    s = ""
    for x in range(1,10):
        s += str(x)


    listes=[]
    
    for n in itertools.permutations(s):
        listes.append(createseq(n))
    
    return listes

def isPal(string):
    return string == string[::-1]

def concatenated(strnum):
    for n in range(1,5):
        a = int(str(strnum)[0:n])
        sb = str(2*a)
        if sb != strnum[len(str(a)):len(str(a))+len(sb)]:
##            print(sb,a,strnum[len(str(a)):len(str(a))+len(sb)])
            pass
        elif len(str(a)) + len(str(sb)) == len(str(strnum)):
            return True
        else:
##            print("sb = 2+a",sb,a)

            sc = str(3*a)
            if len(str(strnum)) >= len(str(a)) + len(sb)+ len(sc):
                if sc != strnum[len(str(a))+len(sb):len(str(a))+len(sb)+len(sc)]:
##                    print(sc,sb,a)
                    pass
                elif len(str(a)) + len(str(sb))+len(str(sc)) == len(str(strnum)):
                    return True
                else:
                    sd = str(4*a)
                    if len(str(strnum)) >= len(str(a)) + len(sb)+ len(sc)+len(sd):
                        if sd != strnum[len(str(a))+len(sb)+len(sc):len(str(a))+len(sb)+len(sc)+len(sd)]:
                            pass
                        else:
                            return True

       


def main():
    start = time.time()
    m = euler38()
    while len(m)>1:
        d = m.pop()
        if concatenated(str(d)):
            print(d)
            break
    end = time.time()
    print(end-start)


main()
