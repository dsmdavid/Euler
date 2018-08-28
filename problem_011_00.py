##Special Pythagorean triplet
##Problem 9
##A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
##
##a2 + b2 = c2
##For example, 32 + 42 = 9 + 16 = 25 = 52.
##
##There exists exactly one Pythagorean triplet for which a + b + c = 1000.
##Find the product abc.


import numpy as np
import time

def pyttrp(number):
    listpossiblevalues =[]
    for i in range(1,number+1):
        listpossiblevalues.append(i)
    listabc = []
##    while (z + x + y) != number and y <((number)/2):
##        z = int((x**2 + y**2)**0.5)
##        for a in range(1, int(number/2+1)):
##            x = a
##            for b in range(1, int(number/2+1)):
##                y=b
##                z = int((x**2 + y**2)**0.5)
##                if (z + x + y) == number and (z**2 == x**2 +y**2):
##                    print("helo",x,y,z, x+y+z, x**2, y**2,z**2)
##                    return (x,y,z)

    for a in listpossiblevalues:
        for b in listpossiblevalues:
            c = number - (a+b)
            if c**2 == a**2 + b**2:
                listabc.append((a,b,c))
        if a%100 ==0:
            print(a)

        listpossiblevalues.remove(a)

##    for a in range(1, int(number)):
##        for b in range(1, int(number)):
##            c = number - (a+b)
##            if c**2 == a**2 + b**2:
##                listabc.append((a,b,c))
##            print(a,b,c, a**2,b**2,c**2)
##        print(a,b)
    return listabc
            
                    
    
        

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


def biggestprod(arrayn, howmanynumbers):
    a = arrayn
    nm = howmanynumbers
    nmax = 0


    for j in range(0, len(a[0])-nm):
        for i in range(0,len(a)):
            k = np.prod(a[i,j:j+nm])
            nmax = max(nmax,k)
            if nmax == k:
                f = a[i,j:j+nm]
    for i in range(0, len(a)-nm):
        for j in range(0,len(a[0])):
            k = np.prod(a[i:i+nm,j])
            nmax = max(nmax,k)
            if nmax == k:
                f = a[i:i+nm,j]

    for j in range(-len(a)+nm,len(a[0]-nm)):
        m = np.diag(a,j)
        for h in range(0, max(1,len(m)-nm)):
            k = np.prod(m[h:h+nm])
            nmax = max(nmax,k)
            if nmax == k:
                f = m[h:h+nm]
                
    a = np.fliplr(a)
    for j in range(-len(a)+nm,len(a[0]-nm)):
        m = np.diag(a,j)
        for h in range(0, max(1,len(m)-nm)):
            k = np.prod(m[h:h+nm])
            nmax = max(nmax,k)
            if nmax == k:
                f = m[h:h+nm]
    return nmax,f
            
##            
##        while len(np.diag(a,j)) >= nm:
##            print(j, np.diag(a,j))
##            for h in range(0, len(np.diag(a,j))-nm):
##                m = np.diag(a,h)
##                k = np.prod(m[h:h+nm])
##                print("m",m)
##                print("m[h:h+nm]",m[h:h+nm])
##                nmax = max(nmax,k)
            
        
                       
    

def main():
    start = time.time()
    a = np.loadtxt("F:\VirtualBOX\DropBox\Dropbox\python\Euler\problem_011_data.txt")
    maxvala, lista = biggestprod(a,4)
 
    print(maxvala)
    print(lista)
    



##    k = primesfrom2to(2000000)
##    print(k)
##    print(len(k))
##    s = 0
##    for i in k:
##        i = int(i)
##        s = s+i
##    print(s)
##    print(np.sum(k, axis=0))
##    palind = findpalind(1000)
##    print(max(palind))
##    minnum = smallestnumber(40)
##    print(minnum)
    
    end = time.time()
    print(end -start)
    
    
    

    
main()
