##The prime 41, can be written as the sum of six consecutive primes:
##
##41 = 2 + 3 + 5 + 7 + 11 + 13
##This is the longest sum of consecutive primes that adds to a prime
##below one-hundred.
##
##The longest sum of consecutive primes below one-thousand that
##adds to a prime, contains 21 terms, and is equal to 953.
##
##Which prime, below one-million, can be written as the sum of
##the most consecutive primes?

import numpy as np
import itertools
import math
import time
import eulertools as et


# 1. Find primes under one million.
# 2. Test for each prime:
#   primes[i] + primes[i+1] +... primes[j] until the sume >= prime.
# if the sum == prime, end, if >, break and start again with primes[i+1].

def euler50(upperlimit):
    primes = et.primesfrom2to(upperlimit)
    primes_rev = primes[::-1]
    print(len(primes))
    dict_c = {}
    
##    print(primes)
    for i in range(0, len(primes_rev)):
        prime = primes_rev[i]
##        if prime == 41:
##            print("start")
        dict_c[prime] = []
        for j in range(0,len(primes)):
            suma = 0
            start = j
            list_primes = []
            
            while suma < prime and primes[j] != prime:
                suma += primes[j]
                list_primes.append(primes[j])
##                print(suma,i,j,prime)
                if j >= len(primes) - i:
##                    print("breaking", prime,j,i)
                    break
                if suma == prime:
##                    print(start,j)
                    dict_c[prime].append(list_primes.copy())
##                    print(prime)
                    break
                
                j += 1
##    print(dict_c)
    maxa = 0
    dict_max =dict()
    for i in dict_c.keys():
        try:
            for j in range(0,len(dict_c[i])):
                tmp_max = len(dict_c[i][j])
                if tmp_max >= maxa:
                    maxa = tmp_max
                    try:
                        m = dict_max[maxa]
                        addme = max(m,i)

                    except:
                        pass
                        
                    dict_max[maxa] = i
        except:
            pass
    
##    print(dict_max)
    
    print(maxa)
    print(dict_max[maxa])
##    print(dict_c[dict_max[maxa]])

        
def main():
    start = time.time()
    euler50(10000)
    end = time.time()
    print(end-start)


main()
