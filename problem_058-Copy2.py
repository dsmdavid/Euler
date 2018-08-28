
# coding: utf-8

# 
# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
# 
# 
# $$
# |37| 36| 35| 34| 33| 32| 31| \\ 
# |38| 17| 16| 15| 14| 13| 30|  \\
# |39| 18|  5|  4|  3| 12| 29|  \\
# |40| 19|  6|  1|  2| 11| 28|  \\
# |41| 20|  7|  8|  9| 10| 27|  \\ 
# |42| 21| 22| 23| 24| 25| 26| \\
# |43| 44| 45| 46| 47| 48| 49|
# $$
# 
# 
# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
# 
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

# #Approach:
# ####1. Create matrix
# ####2. Fill matrix
# ####3. Check if diagonals are prime
# ####4. Calculate %

# In[1]:

import numpy as np
import eulertools


# In[2]:

primes = set(eulertools.primesfrom2to(999999999))
#100000000))#299999999))


# In[3]:

#@profile
def alternate2(primes, val):
    '''Deduce the way the numbers increase as a function of the increased side. Apply that knowdledge to 
    infer the turning point'''
    #intialize
    diagonals = [1,3,5,7,9]
    dist = len(diagonals)
    pmax = max(primes)
    maxd = max(diagonals)
    ratio = 1
    pr_list = [1 if x in primes else 0 for x in diagonals]
    
    prs = sum(pr_list)
    n=3
    
    #loop
    while ratio > val:
        n+=2
    
        if maxd < pmax:
            primes = primes
        else:
            primes = set(eulertools.primesfrom2to(100*pmax))
            pmax = max(primes)
        
        for i in range(1,5):
            value = maxd + i *(n-1)
            #diagonals.append(value)
            if value in primes:
                prs +=1
        #ext_list = [maxd+(n-1), maxd+2*(n-1), maxd + 3*(n-1), maxd+4*(n-1)]
        #ext_pr = [1  if x in primes else 0 for x in ext_list]
        
        #diagonals.extend(ext_list)
        #pr_list.extend(ext_pr)
        
        maxd = maxd + 4*(n-1)
        dist +=4
        ratio = prs/dist
    
        
    
        
    return n, ratio, prs, maxd, dist, pmax#, diagonals
    
    
   # pr_list = [1 for x in diagonals if x in primes else 0]
    


# In[4]:

t = alternate2(primes, 0.1)


# In[5]:

print(t)

