##Largest product in a series
##Problem 8
##Find the greatest product of five consecutive digits in the 1000-digit number.
##
##73167176531330624919225119674426574742355349194934
##96983520312774506326239578318016984801869478851843
##85861560789112949495459501737958331952853208805511
##12540698747158523863050715693290963295227443043557
##66896648950445244523161731856403098711121722383113
##62229893423380308135336276614282806444486645238749
##30358907296290491560440772390713810515859307960866
##70172427121883998797908792274921901699720888093776
##65727333001053367881220235421809751254540594752243
##52584907711670556013604839586446706324415722155397
##53697817977846174064955149290862569321978468622482
##83972241375657056057490261407972968652414535100474
##82166370484403199890008895243450658541227588666881
##16427171479924442928230863465674813919123162824586
##17866458359124566529476545682848912883142607690042
##24219022671055626321111109370544217506941658960408
##07198403850962455444362981230987879927244284909188
##84580156166097919133875499200524063689912560717606
##05886116467109405077541002256983155200055935729725
##71636269561882670428252483600823257530420752963450


import numpy as np
import time


def largestprod(string,length):
    n = 1
    for i in range(0,len(string)-(length)):
        npd = np.arange(1,length+1)
        for j in range(0, len(npd)):
            npd[j] = int(string[i+j])
        n = max(n,np.prod(npd))
    return n
    
    
def smallestnumber(Nmax):
    # find the list of prime numbers in range(Nmax)
    listprimes2ton = primesfrom2to(Nmax)
    # create an array for the factorization
    valueeachprime = np.ones(len(listprimes2ton))
    
    # create an array starting in number 2 ranging to Nmax, type float64
    numbers = np.arange(2,Nmax, dtype=np.float64)
    # factorize each number in the range. Update the factorization_array
    for i in numbers:
        while i not in listprimes2ton:
            eachvalueprime = factorize(i, listprimes2ton)
            for i in range(0,len(valueeachprime)):
                valueeachprime[i] = max(valueeachprime[i],eachvalueprime[i])

    valuearray = listprimes2ton**valueeachprime

    # Calculate the least common multiple: with np.prod() I get an error or
    # inconsistent results. I've tried several dtype = int, np.float64, but still get the error.
    # So I use an alternative:
    value = 1
    for i in valuearray:
        value = value * i
    print(listprimes2ton)
    print(valueeachprime)

    return value

    
def factorize(n,listofprimes):

    valueeachprime = np.zeros(len(listofprimes))
    for i in range(1, len(listofprimes)):
        while n >= listofprimes[i-1] and n % listofprimes[i-1] == 0:
            n = n / listofprimes[i-1]
            valueeachprime[i-1] = valueeachprime[i-1] + 1

    return valueeachprime



def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    if n%2 == 0:
        return "x2"
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

    l = str(
        7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
        )
    print(largestprod(l,5))
##    palind = findpalind(1000)
##    print(max(palind))
##    minnum = smallestnumber(40)
##    print(minnum)
    
    end = time.time()
    print(end -start)
    
    
    

    
main()
