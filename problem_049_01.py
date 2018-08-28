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

def getpermutationlist(listn):
    return [int(concate(x)) for x in itertools.permutations(listn)]

def concate(tuple_l):
	string = ""
	for i in range(0,len(tuple_l)):
		string += tuple_l[i]
	return string

def euler49(end):
    primes = et.primesfrom2to(10000)
    primes = primes[::-1]
    print(len(primes))
    count = 0
    check = 0
    dict_c = {}
    checked = set()
    for prime in primes:
        if prime in checked:
            pass
        elif len(str(prime))<4:
            pass
        else:
            listn = [x for x in str(prime)]
            listn = set(getpermutationlist(listn))
            listn = [x for x in listn]
            listn = sorted(listn,reverse=True)
##            print(listn)
            for next_prime in listn:
                if len(str(next_prime)) < 4:
                    pass
                elif next_prime < prime and next_prime in primes:
##                    checked.add(next_prime)

##                    print(prime,next_prime)
                    a = prime - next_prime
                    b = next_prime - a
                    if len(str(b)) < 4:
                        pass
                    elif b in primes and b in listn:
                        dict_c[count]=[prime, next_prime, b, a]
                        count += 1
                    else:
                        pass
                else:
                    pass
            
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
