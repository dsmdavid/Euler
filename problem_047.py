##Distinct primes factors
##Problem 47
##The first two consecutive numbers to have two distinct prime factors are:
##
##14 = 2 × 7
##15 = 3 × 5
##
##The first three consecutive numbers to have three distinct prime factors are:
##
##644 = 2² × 7 × 23
##645 = 3 × 5 × 43  
##646 = 2 × 17 × 19.
##
##Find the first four consecutive integers to have four distinct prime factors.
##What is the first of these numbers?

import numpy as np
import itertools
import math
import time
import eulertools as et


## 1. For each number, try:
## isPrime? if it is, add to the prime list.
## if it is not prime:
## Divide the number by the first prime (not 1). while % ==0, add prime to list
## and set of divisors, and repeat.
## if not, try the next, while the combined accumulated product < number.
## if the combined accumulated product == number (all the divisors are found),
## break.


## if the length of the set of divisors == 4, try with the next number, then
## the following and the next one.

def test_arr2(number,npprimes,np_opd):
    for i in npprimes:
        if number % i == 0:
            np_opd = np.append(np_opd,i)
            number = number/i
            number,npprimes,np_opd = test_arr(number,npprimes,np_opd)
        else:
            npprimes = np.delete(npprimes,0)
        if number < i:
            break         

    return number,npprimes,np_opd


def test_arr(number,npprimes,np_opd):
    for i in npprimes:
        if number % i == 0:
            np_opd = np.append(np_opd,i)
            number = number/i
            number,npprimes,np_opd = test_arr(number,npprimes,np_opd)
##        else:
##            npprimes = np.delete(npprimes,0)
        if number < i:
            break         

    return number,npprimes,np_opd


def divisors(number, npprimes):
    
    np_opd = np.array([],dtype=np.int32)
    number,npprimes,np_opd = test_arr(number,npprimes,np_opd)    
        
    return np_opd #np.array that contains all the prime factors

def euler47(n_divisors,n_consecutive):
    count = 0
    primes = et.primesfrom2to(1000)
    n = 3
    flag = True
    while flag == True:
        if n not in primes:
            np_opd = divisors(n,primes)
            primeset = set(np_opd)
            if len(primeset) == n_divisors:
                count += 1
##                print(n,np_opd,primeset)
            else:
                if count != 0:
                    count = 0
            if count == n_consecutive:
                print(n-count+1,np_opd,primeset)
                flag = False
        else:
            count = 0
        n += 1
                   

def testme():
    number = 645
    npprimes = et.primesfrom2to(1000)
    np_opd = np.array([], dtype = np.int32)
    n,npp,np_opd = test_arr(number,npprimes,np_opd)
    print(np_opd)


def testme1():
    number = 644
    npprimes = et.primesfrom2to(1000)
    np_opd = np.array([], dtype = np.int32)
    n,npp,np_opd = test_arr1(number,npprimes,np_opd)
    #print(np_opd)

def main():
    start = time.time()
    ##    testme()
    euler47(4,4)
    end = time.time()
    print(end-start)


main()
