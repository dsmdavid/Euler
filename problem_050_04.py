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
    primeset = set(primes)
    primes_rev = primes[::-1]
    print("len(primes)\t",len(primes))
    print("primes[len(primes)/2]\t",primes[len(primes)/2])
    print("primes[len(primes)-1]\t",primes[len(primes)-1])
    print("sum(primes)\t",sum(primes))
    print("sum(primes[0:len(primes)/2])\t",sum(primes[0:len(primes)/2]))
    dict_c = {}
    #input("break")
    max_summs = 0
    current = []
    max_prime = 1
    for i in range(0, len(primes_rev)):
        prime = primes_rev[i]
        set_tried =set()
##        dict_c[prime] = []
        for j in range(0,len(primes)):
            suma = 0
            start = j
            list_primes = []
            count = 0
                        
            while suma < prime and primes[j] != prime:
                
                count += 1
                suma += primes[j]
                if suma in set_tried:
                    break
                list_primes.append(primes[j])
                if suma in primeset:
                    set_tried.add(suma)
                if j >= len(primes) - i:
                    break
                if suma == prime:                    
                    if count > max_summs:
                        max_summs = count
                        current = list_primes.copy()
                        max_prime = prime
                        try:
                            dict_c[prime].append(list_primes.copy())
                        except:
                            dict_c[prime] = list_primes.copy()
                    break
                
                j += 1
                
    print(max_summs)
##    print(current)
    print(max_prime)

def euler50b(upperlimit):

# 1. Find primes under one million.
# 2. Test for each prime:
#   primes[i] + primes[i+1] +... primes[j] until the sume >= prime.
# if the sum == prime, end, if >, break and start again with primes[i+1].


    #create the list of primes
    primes = et.primesfrom2to(upperlimit)
    primeset = set(primes)
    primes_rev = primes[::-1]
    print("len(primes)\t",len(primes))
    print("primes[len(primes)/2]\t",primes[len(primes)/2])
    print("primes[len(primes)-1]\t",primes[len(primes)-1])


#[a,b,c,...,n-1,n]
# while t_sum < 10^6: increase t_sum with next prime.
# t_sum = a + b + c + ... + (n-1) + n
# once t_sum > 10^6, go back to t_sum < 10^6.
# if t_sum not prime, subtract:
# (a)
# if (t_sum-a) not prime, try: (t_sum-n)
# if that is not prime, try: t_sum - a - n, or t-sum-a-b, or t_sum - n - (n-1)
# etc. until the result is prime.
# repeat starting with "b", as long as the list of primes that
# sum up to <10^6 is longer than the list of primes that sum to
# the last prime.

    
    max_summs = 0
    max_prime = 1
    


##    print("sum(primes)\t",sum(primes))
##    print("sum(primes[0:len(primes)/2])\t",sum(primes[0:len(primes)/2]))
    dict_c = {}
    #input("break")
    max_summs = 0
    current = []
    max_prime = 1
      
    for i in range(0, len(primes_rev)):
        prime = primes_rev[i]
        set_tried =set()
##        dict_c[prime] = []
        for j in range(i+1,len(primes_rev)-1):
            diff = prime
            start = j
            list_primes = []
            count = 0
                        
            while diff > 0 and j <len(primes_rev):
                
                count += 1
                try:
                    diff -= primes_rev[j]
                except:
                    print(diff,i,j,len(primes_rev))
                if diff in set_tried:
                    break
                list_primes.append(primes_rev[j])
                if diff in primeset:
                    set_tried.add(diff)
##                if j >= len(primes) - i:
##                    break
                if diff == 0:                    
                    if count > max_summs:
                        max_summs = count
                        current = list_primes.copy()
                        max_prime = prime
                        try:
                            dict_c[prime].append(list_primes.copy())
                        except:
                            dict_c[prime] = list_primes.copy()
                    break
                
                j += 1
                
    print(max_summs)
##    print(current)
    print(max_prime)
    print(dict_c[max_prime])
##    maxa = 0
##    dict_max =dict()
##    for i in dict_c.keys():
##        try:
##            for j in range(0,len(dict_c[i])):
##                tmp_max = len(dict_c[i][j])
##                if tmp_max >= maxa:
##                    maxa = tmp_max
##                    try:
##                        m = dict_max[maxa]
##                        addme = max(m,i)
##
##                    except:
##                        pass
##                        
##                    dict_max[maxa] = i
##        except:
##            pass
##    
##    
##    print(maxa)
##    print(dict_max[maxa])
##    print(dict_c[dict_max[maxa]])


def euler50c(upperlimit):

# 1. Find primes under one million.
# 2. Test for each prime:
#   primes[i] + primes[i+1] +... primes[j] until the sume >= prime.
# if the sum == prime, end, if >, break and start again with primes[i+1].


    #create the list of primes
    primes = et.primesfrom2to(upperlimit)
    primeset = set(primes)
    primes_rev = primes[::-1]
    print("len(primes)\t",len(primes))
    print("primes[len(primes)/2]\t",primes[len(primes)/2])
    print("primes[len(primes)-1]\t",primes[len(primes)-1])
    max_prime = 2
    current_max = 0
    start_position = 0
    dict_c = {}
    vector_primes = np.zeros(upperlimit)
    for i in primes:
        vector_primes[i] = 1

    for starting in range(0,len(primes)):
        temp_max, temp_max_list, initial,end = rec_sum2(primes,vector_primes,upperlimit,start_position = starting,current_max = current_max)
        if temp_max_list > current_max:
            current_max = temp_max_list
            max_prime = temp_max
            dict_c[max_prime] = current_max
    print(max_prime,current_max)

def rec_sum2(list_primes,vector_primes,upperlimit,start_position,current_max):
    """ Receives a list of consecutive primes, an upperlimit --max value admitted--
    the starting position in the 'list of primes', and the
    current maximum of summands found.
    Returns the prime that can be constructed as the longest sum of consecutive
    primes given those conditions."""
    
    primes = list_primes
    vector = vector_primes
    t_sum = 0
    start_p = start_position

    
    while t_sum < upperlimit:
        t_sum += primes[start_p]
##        
##            print(t_sum, upperlimit, start_p, len(primes), start_position)
##            input()
        if start_p + 1 < len(primes):
            start_p += 1
        else:
            break
    if t_sum >= upperlimit:
        t_sum -= primes[start_p-1]
        start_p = start_p - 1

    t_value = t_sum
    value = 0
    i = j = 0
    while vector[t_value]== 0 and (((start_p-j)- (start_position+i))>current_max):
        for i in range(0,value+1):
            for j in range(0,value-i+1):
                # proceed only if the potential list is longer than the existing
                if current_max > ((start_p-j)- (start_position+i)):
                    break
                if i == 0:
                    sum_i = 0
                else:
                    sum_i = sum(primes[start_position:start_position+i])
                if j == 0:
                    sum_j = 0
                else:
                    sum_j = sum(primes[start_p-j:start_p])
                t_value = t_sum - sum_i - sum_j
                
        value += 1

    if current_max < ((start_p-j)- (start_position+i)) and vector[t_value]==1:
        current_max = ((start_p-j)- (start_position+i))
        return t_value, current_max, (start_position + i), (start_p - j)
    else:
        return 2, current_max, 0, 0

def rec_sum(list_primes,upperlimit,start_position,current_max):
    """ Receives a list of consecutive primes, an upperlimit --max value admitted--
    the starting position in the 'list of primes', and the
    current maximum of summands found.
    Returns the prime that can be constructed as the longest sum of consecutive
    primes given those conditions."""
    
    primes = list_primes
    t_sum = 0
    start_p = start_position

    
    while t_sum < upperlimit:
        t_sum += primes[start_p]
##        
##            print(t_sum, upperlimit, start_p, len(primes), start_position)
##            input()
        if start_p + 1 < len(primes):
            start_p += 1
        else:
            break
    if t_sum > upperlimit:
        t_sum -= primes[start_p-1]
        start_p = start_p - 1
## do the operations here
        ##

# value = 1:
# i) -a (1,0)
# ii) -n (0,1)
# value = 2:
# i) -a -b (2,0)
# ii) -a - n (1,1)
# iii) -n - n-1 (0,2)
# value = 3:
# i) -a -b -c (3,0)
#ii) -a -b -n (2,1)
#iii) -a -n - n-1 (1,2)
#iv) -n -n-1 -n-2 (0,3)
    t_value = t_sum
    value = 0
    i = j = 0
    while t_value not in primes and (((start_p-j)- (start_position+i))>current_max):
        for i in range(0,value+1):
            for j in range(0,value-i+1):
                # proceed only if the potential list is longer than the existing
                if current_max > ((start_p-j)- (start_position+i)):
                    break
                if i == 0:
                    sum_i = 0
                else:
                    sum_i = sum(primes[start_position:start_position+i])
                if j == 0:
                    sum_j = 0
                else:
                    sum_j = sum(primes[start_p-j:start_p])
                t_value = t_sum - sum_i - sum_j
                
        value += 1
        
    if current_max < ((start_p-j)- (start_position+i)) and t_value in primes:
        current_max = ((start_p-j)- (start_position+i))
        return t_value, current_max, (start_position + i), (start_p - j)
    else:
        return 2, current_max, 0, 0
    

        
def main():
    start = time.time()
    euler50c(1000000)
    end = time.time()
    print(end-start)


main()
