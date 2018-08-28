##Problem 46
##It was proposed by Christian Goldbach that every odd composite number
##can be written as the sum of a prime and twice a square.
##
##9 = 7 + 2×12
##15 = 7 + 2×22
##21 = 3 + 2×32
##25 = 7 + 2×32
##27 = 19 + 2×22
##33 = 31 + 2×12
##
##It turns out that the conjecture was false.
##
##What is the smallest odd composite that cannot be written as the sum
##of a prime and twice a square?


import numpy as np
import itertools
import math
import time
import eulertools as et


## 1. For each number, try:
## isPrime? if it is, add to the prime list.
## if it is not prime:
##  Number - each prime lower than number.
##  if sqrt(result/2) is integer, go to next odd number
##  if not, go to next prime until next prime is greater than number.
## print that number



def euler46():
    n = 3
    primes = et.primesfrom2to(1000000)
    flag = True
    while flag == True:
        if n not in primes:
            check = 0
            # small numbers only, I will increase primes only if needed.
            for i in primes:
                if i < n:
                    try:
                        result = n - i
##                        print('testing... ' + str(n) + ' ' + str(i))
                        if int(np.sqrt(result/2)) == np.sqrt(result/2):
##                            print(n,i)
                            check = 1

                            break
                    except:
                        print("error in try")
            if check == 0:
                print(n)
                flag = False
        n += 2
##        if n > 40:
##            flag = False
##                        
                

                    

    

def main():
    start = time.time()
    euler46()

    end = time.time()
    print(end-start)


main()
