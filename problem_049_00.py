##The arithmetic sequence, 1487, 4817, 8147, in which each of the
##terms increases by 3330, is unusual in two ways: (i) each of the
##three terms are prime, and, (ii) each of the 4-digit numbers are
##permutations of one another.
##
##There are no arithmetic sequences made up of three 1-, 2-, or
##3-digit primes, exhibiting this property, but there is one
##other 4-digit increasing sequence.
##
##What 12-digit number do you form by concatenating the three terms
##in this sequence?

import numpy as np
import itertools
import math
import time
import eulertools as et


# 1. Find all 4-digit primes.
# 2. Test for each prime if:
#  Prime - next(prime) = a -> is  next(prime) - (a) in the prime set?
# Is the set of digits the same in the three of them?


def euler49(end):
    primes = et.primesfrom2to(10000)
    print(len(primes))
    count = 0
    check = 0
    dict_c = {}
    for prime in primes:
        for next_prime in primes:
            if next_prime < prime:
                if set(str(next_prime)) == set(str(prime)):
                    a = prime - next_prime
                    b = next_prime - a
                    if b in primes:
                        if set(str(b)) == set(str(prime)):
                            dict_c[count]=[prime, next_prime, b, a]
                            count += 1
            else:
                break
        if check == len(primes)/3:
            print(check,prime)
        check += 1
    print(dict_c)
        
def main():
    start = time.time()
    euler49(1000)
    end = time.time()
    print(end-start)


main()
