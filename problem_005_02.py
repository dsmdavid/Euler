##Smallest multiple
##Problem 5
##2520 is the smallest number that can be divided by each of the numbers
##from 1 to 10 without any remainder.
##
##What is the smallest positive number that is evenly divisible by all
##of the numbers from 1 to 20?

import numpy as np
import time

def smallestnumber(Nmax):
    # find the list of prime numbers in range(Nmax)
    listprimes2ton = primesfrom2to(Nmax)
    # create an array starting in number 2 ranging to Nmax, type float64 to
    # avoid stack overflow
    numbers = np.arange(2,Nmax, dtype=np.float64)
    # this is the maximum number
    maxnumber =int(np.prod(numbers))
##    for x in numbers:
##        maxnumber = maxnumber * x
    print(maxnumber)
    # loop to reduce the maxnumber / i for each of the prime numbers
    for i in listprimes2ton:
        test_ar = np.ones(len(numbers),dtype=bool)
        print(i,test_ar)
        i = int(i)

        print(maxnumber % i ==0)
        print(numbers)
        print(type(maxnumber),type(i))
        print("a", maxnumber % numbers)
        print("b",(maxnumber/i % numbers == 0).all())
        # only if the division by i has module 0 and if that number divided
        # by all the numbers in the range 2-Nmax also has module 0
        while maxnumber % i == 0 and ((maxnumber/i) % numbers == 0).all():
                maxnumber = maxnumber / i
                print(maxnumber, i)
             

    return maxnumber
    
    


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    for i in range(1,int((n**0.5)/3+1)):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]



def calculatedivisors(maxlimit):
    npdivisors = []
    k = 0
    while k == 0:

        for i in range(2, int(maxlimit/2)):

            if maxlimit % i == 0:
                npd = np.ones(len(npdivisors), dtype=bool)
                m = 0
                try:
                    for j in npdivisors:
                        if i % j == 0:
                            npd[m] = False                
                            break
                        m += 1
                    if npd.all():
                        npdivisors.append(i)
                        product = 1
                        for element in npdivisors:
                            product = element * product
                        if product == maxlimit:
                            k = 1
                            return npdivisors
                        
                            
                except:
                    npdivisors.append(i)
            
            



    print(npdivisors)

    return npdivisors
            

def findpalind(Nmax):
    list1 = []
    for i in range(1, Nmax):
        list1.append(i)
    list1.reverse()
    list2 = list1[:]
    listpalind = set()
    m = 0
    while m == 0:
        for i in list1:
            for j in list2:
                k = i * j
                if str(k) == str(k)[::-1]:
##                    print("str(k) == str(k)[-1:1]", str(k), str(k)[::-1])
                    listpalind.add(k)
##                    print("appending ", k)
                    m = 1
##                    print(listpalind)
    return listpalind
                
def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s == s[::-1]
def checkpals(Nmax):
    val = 0
    for i in range(Nmax,1,-1):
        for j in range(Nmax,1,-1):
            if isPal(str(i*j)) and i*j > val:
                val = i*j
    return val
            

def main():
    start = time.time()
##    palind = findpalind(1000)
##    print(max(palind))
    minnum = smallestnumber(20)
    print(minnum)
    
    end = time.time()
    print(end -start)
    
    
    

    
main()
