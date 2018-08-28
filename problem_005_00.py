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
    numbers = np.arange(2,Nmax, dtype=np.float64)
    maxnumber = int(np.prod(numbers))
    print(maxnumber)
    for i in listprimes2ton:
        test_ar = np.ones(len(numbers),dtype=bool)
        print(i,test_ar)
        print(maxnumber % i ==0)
        print(numbers)
        print(maxnumber % numbers)
        print((maxnumber % numbers == 0).all())
        while maxnumber % i == 0 and ((maxnumber/i) % numbers == 0).all():
                maxnumber = maxnumber / i
                print(maxnumber, i)
                
##        if maxnumber % i == 0:
##            nmaxnumber = int(maxnumber/i)
##            print(nmaxnumber, maxnumber, i)
##            test_ar = (nmaxnumber % numbers == 0)
##            print(test_ar)
##            while test_ar.all():
##                print(test_ar)
##                nmaxnumber = maxnumber/i
##                print(nmaxnumber, maxnumber, i)
##                test_ar = (nmaxnumber % numbers == 0)
##                if test_ar.all():
##                    print(maxnumber)
##                    maxnumber = nmaxnumber
##                    print(maxnumber)

##    minnumb = listprimes2ton.prod(axis=0)
##    print(minnumb)
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


def delbart(t,n):
    if n > 0:
        print(t)
        if not (t%n):
            if delbart(t, n-1):
                return True
            else:
                return False
        else:
            return False
    else:
        return True



def main():
    start = time.time()
##    palind = findpalind(1000)
##    print(max(palind))
##    minnum = smallestnumber(20)
##    print(minnum)
##    
    i = 20
    while not delbart(i,20):
        i +=20
    print(i)
    end = time.time()
    print(end -start)


    
    

    
main()
