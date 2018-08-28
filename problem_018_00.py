##Maximum path sum I
##Problem 18
##By starting at the top of the triangle below and moving
##to adjacent numbers on the row below, the maximum total
##from top to bottom is 23.
##
##3
##7 4
##2 4 6
##8 5 9 3
##
##That is, 3 + 7 + 4 + 9 = 23.
##
##Find the maximum total from top to bottom of the triangle below:
##
##75
##95 64
##17 47 82
##18 35 87 10
##20 04 82 47 65
##19 01 23 75 03 34
##88 02 77 73 07 63 67
##99 65 04 28 06 16 70 92
##41 41 26 56 83 40 80 70 33
##41 48 72 33 47 32 37 16 94 29
##53 71 44 65 25 43 91 52 97 51 14
##70 11 33 28 77 73 17 78 39 68 17 57
##91 71 52 38 17 14 91 43 58 50 27 29 48
##63 66 04 68 89 53 67 30 73 16 69 87 40 31
##04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
##
##NOTE: As there are only 16384 routes, it is possible to solve
##this problem by trying every route. However, Problem 67, is
##the same challenge with a triangle containing one-hundred rows; it
##cannot be solved by brute force, and requires a clever method! ;o)
##

import numpy as np
import time
##
##DICTNUMB = {
##    1: "one",
##    2: "two",
##    3: "three",
##    4: "four",
##    5: "five",
##    6: "six",
##    7: "seven",
##    8: "eight",
##    9: "nine",
##    10: "ten",
##    11: "eleven",
##    12: "twelve",
##    13: "thirteen",
##    14: "fourteen",
##    15: "fifteen",
##    16: "sixteen",
##    17: "seventeen",
##    18: "eighteen",
##    19: "nineteen",
##    20: "twenty",
##    30: "thirty",
##    40: "forty",
##    50: "fifty",
##    100: "hundred",
##    1000: "onethousand"
##    }
##DICTLENG = {}
##for i in DICTNUMB.keys():
##    DICTLENG[i] = len(DICTNUMB[i])
##print(DICTLENG)
def sumstringnumber(number):
    a = int(number)
    b = str(a)
    z = 0
    for i in range(0, len(b)):
        z += int(b[i])

    return z

def collatz(number):
    maxcount = 0
    count = 1
    dictcoll = {1:0}
    dictmax = 0
    for i in range(2,number):
        a = i
        while i > 1:
            if i in dictcoll.keys():
                count += dictcoll[i] -1
                break
            elif i%2==0:
                i = i/2
                count +=1
            else:
                i = 3*i + 1
                count +=1

        dictcoll[a] = count
        maxcount = max(count, maxcount)
        if count == maxcount:
            dictmax = a

        count = 1
    return dictmax

def collatz2(number, maxv, cached):
    number = int(number)


    if number < maxv and cached[number] != None:
        return cached[number]
    elif number % 2 ==0:
        temp = 1 + collatz2(number/2, maxv, cached)
    else:
        temp = 1 + collatz2(number*3 + 1, maxv, cached)
    if number < maxv:
        cached[number] = temp
    return temp


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
            
        
                       
##def calculatedivisorsnotconsecutive(n):
##    npdivisors = 1 # The biggest divisor is n itself.
##    # This is slower
####    a = n/2 + 1
####    b = 1
####    while b < a:
####        if n%b == 0:
####            npdivisors +=1
####        b +=1
####    
##    for i in range(1, int(n/2 +1)):
####        if n % i == 0:
####            npdivisors += 1         
####            
##
##    return npdivisors
def calculatedivisorsnotconsecutive(n):
    npdivisors = []    
    for i in range(1, int(n/2 +1)):
        if i in npdivisors:
            break
        else:
            if n % i == 0:
                npdivisors.append(i)
                npdivisors.append(n/i)
            
    return npdivisors

def readfromfilesamplenames(filename):

    fo = open(filename,"r")
    list1 =[]
    for line in fo:
        list1.append(line.replace("\n", ""))
    fo.close()

    return list1

def sumbigarray(array, number):
    n = number
    h = array
    k = len(h)
    z = a = np.int64(0)
    m = []
    for i in range(0, k):
        r = k-i-1
        b = array[r] + a
        m.append(b)
##        print(str(h[r]),str(h[r])[:-3])
        a = int(str(h[r])[:-3])
    m.reverse()
    print(m)
    for i in range(0, n):
        print(i, n, m[n-i-1])
        print(int(m[n-i-1]),int(m[n-i-1])**i)
        z += int(m[n-i-1])**int(i)
        print(z)
    return m, z


def getChildren(x,y,dictChildren):
    """Going through coordinates:
    Each node has two children:
    [
    11 - 12 - 13 ... 1(n-1) - 1n
    21 - 22 - 23 ... 2(n-1) - 2n
    ...
    i1 - i2 - i3 ... i(n-1) - in
    ...
    n1 - n2 - n3 ... n(n-1) - nn
    ]

    The only available moves from one node
    to its children are: right (xy -> x(y+1))
    or: down (xy -> (x+1)y)
    """
    x1,y1 = x, y+1 ## Right.
    x2,y2 = x+1, y ## Down.
##    print(x,y,x1,y1,x2,y2)
    return x1,y1,x2,y2

def assignValueNode(x,y, maxx, maxy,dictChildren):
    if (x,y) in dictChildren.keys():
##        print(x,y,"returning from dictionary...", dictChildren[(x,y)])
        return dictChildren[(x,y)]
    elif x == maxx or y == maxy:
##        print(x,y,"returning 1")

        return 1
        
    else:
##        print(dictChildren)
        x1,y1,x2,y2 = getChildren(x,y,dictChildren)
##        print(dictChildren)
        dictChildren[(x,y)] = assignValueNode(x1,y1,maxx,maxy,dictChildren) + assignValueNode(x2,y2,maxx,maxy,dictChildren)        
        return assignValueNode(x1,y1,maxx,maxy,dictChildren) + assignValueNode(x2,y2,maxx,maxy,dictChildren)
def calculateNumberLen(x):
    st = 0
    if x not in DICTLENG.keys():
##        print(x, end=" ")
        z = str(x)
        a = len(z)
        if a < 3: ## Number below 100, a == 2 because all single digits are in dict.
            b = int(z[0]+"0")
            if b in DICTLENG.keys():
                st = DICTLENG[b] # length of the string.
##                print(b, "is in DICTLENG and has a value of ", st)
            else:
                if z[0] == "0":
                    pass
                    ##                    print(b, "is NOT in DICTLENG", end=" ")
                    
                elif z[0] != "8":
                    st = DICTLENG[int(z[0])] + 2 # ninety = nine + ty
##                    print(z, st)
                else:
                    st = DICTLENG[int(z[0])] + 1 # eighty = eight + y
##                    print(z, st)
                    
            try:
                c = int(z[1])
            except:
                c=0
            if c != 0:
                st += DICTLENG[c]

        elif a == 3: ## Number between 100 and 1000 [100,1000)
            
            st = DICTLENG[int(z[0])] + DICTLENG[100]
            if x % 100 != 0:
                st +=3 ## and

            st += calculateNumberLen(int(z[1:3]))

    else:
        st = DICTLENG[x]
        if x == 100:
            st += 3
##    print(x, st)      
    return st

def convertToPyramid(lista):
    listb = []
    for i in range(0,len(lista)):
        listc = []
        split = lista[i].split(" ")
        for e in split:
            listc.append(int(e))
        listb.append(listc)

    return listb

def calculateMaxPath(testArray,starting):

    sample = testArray
    startingi = starting[0]
    startingj = starting[1]
    valPath = {}
##    print(valPath)

    ## Initialize the dictionary from the starting i,j
    ## to use it as the apex of the ensuing calculations:
    valPath[startingi] = {x: [0,[]] for x in range(0,len(sample[startingi]))}
##    print(valPath)

    valPath[startingi][startingj] = [sample[startingi][startingj], [(startingi,startingj)]]
##    print(valPath)
##
##    print(valPath)
##    print(valPath[startingi])
##    print(valPath[startingi][startingj][0], "this is 1 ", valPath[startingi][startingj][1])

    for i in range(startingi,len(sample)-1):
##        print(i)
##        print(valPath[i])
        valPath[i+1] = {x:[0,[]] for x in range(0,len(sample[i+1]))}
##        print(len(sample[i]), len(sample[i+1]))
        for j in range(0, len(valPath[i+1].keys())):
            if j == 0:
                valPath[i+1][j] = [valPath[i][j][0] + sample[i+1][j], valPath[i][j][1] + [(i+1,j)]]
            elif j >= len(valPath[i]):
                valPath[i+1][j] = [valPath[i][j-1][0] + sample[i+1][j], valPath[i][j-1][1] + [(i+1,j)]]
            else:
                a1 = valPath[i][j][0] + sample[i+1][j]
                a2 = valPath[i][j][1] + [(i+1,j)]
                b1 = valPath[i][j-1][0] + sample[i+1][j]
                b2 = valPath[i][j-1][1] + [(i+1,j)]
                if a1 > b1:
                    input1 = a1
                    input2 = a2
                else:
                    input1 = b1
                    input2 = b2
                valPath[i+1][j] = [input1, input2]
    return valPath

        
        
        

        
def main():
    start = time.time()

    a = readfromfilesamplenames("F:\\VirtualBOX\\DropBox\\Dropbox\\python\\Euler\\problem_018_data.txt")
##    print(a)
    testArray = convertToPyramid(a)
    b = calculateMaxPath(testArray,(0,0))
    listvals = {}
##    print(b)
    for e in b[len(b)-1].keys():
        listvals[b[len(b)-1][e][0]] = [b[len(b)-1][e][1]]
        
    print(max(listvals.keys()))
    print(listvals[max(listvals.keys()) ])

##    t = 0
##    for i in range(1,1001):
##        t += calculateNumberLen(i)
##    print(t)
    
##    maxx = 20
##    maxy = 20
##    dictChildren = {(maxx,maxy):0}
##    print(assignValueNode(0,0,maxx,maxy,dictChildren))
##    maxv = 1000000
##    print(sumstringnumber(2**1000))
    
##    cached = [None] * maxv
##    cached[1] = 1
##    maxlen = 0
##    maxind = None
##    for item in range(1,maxv):
##        a = collatz2(item,maxv, cached)
##        if a > maxlen:
##            maxlen = a
##            maxind = item
##    print(maxind)
##return dictcoll, dictmax, maxcount
##    print(collatz(maxv))
##    print(a)
##    print(b)
##    print(c)
##    print(b[c])
##    n = 6
##    i = 4
##    n = 1249975000 #6
##    i = 50000 #4
##    a = 0
##    j = 50001
##    for b in range(i,j-i):
##        a +=b
##    mi = n + i*(j-i) + a
##    print(mi,a,calculatedivisorsnotconsecutive(mi))
##    while len(calculatedivisorsnotconsecutive(n)) < 500:
##        n = (n) + i
##        i +=1

##    print("The end")    
##    print(n, i)
##    print(calculatedivisorsnotconsecutive(n))
##
##    a = readfromfilesamplenames("F:\VirtualBOX\DropBox\Dropbox\python\Euler\problem_013_data.txt")
##    b = []
##    for e in a:
##        b.append(int(e))
##    c = np.array(b)
####    print(b,c)
##    
##    b = 0
##    for item in a:
####        b += int(item)
####    print(b)
####    print("a", a)
##    k = np.sum(c)
####    print("c",c)
##    print("k",k)
##    
####    b = np.ones((len(a), len(a[0])))
######    b = np.reshape(b, (len(str(a)),len(a[0])))
##    for i in range(0,len(a)):
##        for j in range(0, len(a[i])):
##            b[i,j] = a[i][j]
##    print(a)
##    print(b)
##    print("lena", len(a), "len(a[0])", len(a[0]),"lenb",len(b))
##    h = np.sum(b,axis=1)
##    print(h)
##    testme = np.float64(0)
##    for i in a:
##        testme += np.float64(i)
##    print("solution",i)
##    print(len(str(i)))
##    print("the first 10 digits...",str(i)[0:10:1])
##    kk, k2 = sumbigarray(h, 10)
##
####    v = 0
##    for i in range(0, len(h)):
##        k = len(h)
##        r = k-i-1
##
##        z = (h[r])*(10**i)
##        v +=  z
####        print(h[r],i,k,r,z, v)
##    print("solution...", str(v)[0:11])
##print(z)

                 
   



    
##    a = np.loadtxt("F:\VirtualBOX\DropBox\Dropbox\python\Euler\problem_011_data.txt")
##    maxvala, lista = biggestprod(a,4)
## 
##    print(maxvala)
##    print(lista)
##    



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
