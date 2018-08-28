##Largest prime factor
##Problem 3
##The prime factors of 13195 are 5, 7, 13 and 29.
##
##What is the largest prime factor of the number 600851475143 ?

import numpy as np
import timeit

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int((n**0.5)/3+1)):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]



def calculatedivisors(maxlimit):
    divisors = []
    npdivisors = set()
##    npdivisors.add(2)
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
                        npdivisors.add(i)
##                        print("Appending ",i)
                        product = 1
                        for element in npdivisors:
##                            print(element)
                            product = element * product
##                            print(product)
                        if product == maxlimit:
                            k = 1
##                            print("got it")
                            return npdivisors
                        
                            
                except:
                    npdivisors.add(i)
            
            



    print(npdivisors)
##    print(divisors)
    return npdivisors
            

def main():
    listdivisors = calculatedivisors(int(600851475143
                                   ))
    print(max(listdivisors))
    
    ##listprime = calculateprime(int(600851475143))
##    print(max(listprime))
    print("timing...")
    t = timeit.Timer("calculatedivisors(int(600851475143))","from __main__ import calculatedivisors")

    print(t.timeit())
    print("job done")

main()
