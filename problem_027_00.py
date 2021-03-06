##
##Euler discovered the remarkable quadratic formula:
##
##n² + n + 41
##
##It turns out that the formula will produce 40 primes for
##the consecutive values n = 0 to 39. However, when n = 40,
##402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41,
##41² + 41 + 41 is clearly divisible by 41.
##
##The incredible formula  n² − 79n + 1601 was discovered,
##which produces 80 primes for the consecutive values n = 0 to 79.
##The product of the coefficients, −79 and 1601, is −126479.
##
##Considering quadratics of the form:
##
##n² + an + b, where |a| < 1000 and |b| < 1000
##
##where |n| is the modulus/absolute value of n
##e.g. |11| = 11 and |−4| = 4
##Find the product of the coefficients, a and b, for the quadratic expression
##that produces the maximum number of primes for consecutive values of n,
##starting with n = 0.
    
import numpy as np
import time
import functools
import math
import itertools


def sumstringnumber(number):
    a = int(number)
    b = str(a)
    z = 0
    for i in range(0, len(b)):
        z += int(b[i])
    # Alternatively:
    # import math
    # z = sum(int(x) for x in str(number)

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
            
            



##    print(npdivisors)

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
    for i in range(1, int(math.sqrt(n)+1)):
        if i in npdivisors:
            break
        else:
            if n % i == 0:
                npdivisors.append(int(i))
                npdivisors.append(int(n/i))
            
    return npdivisors

def calculatedivisorsnotconsecutivenoself(n):
    npdivisors = {1}    
    for i in range(2, int(math.sqrt(n)+1)):
        if i in npdivisors:
            break
        else:
            if n % i == 0:
                npdivisors.add(int(i))
                npdivisors.add(int(n/i))
            
    return npdivisors

def readfromfilesamplenames(filename):

    fo = open(filename,"r")
    list1 =[]
    for line in fo:
        list1.append(line.replace("\n", "").replace('"',"").split(","))
    fo.close()

    return list1[0]

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

def countDayofWeek(dayoftheweek, dayofthemonth,startingday,startingmonth,startingyear,endday,endmonth,endyear):
    """ Each year has 365 days, except leap years, that have 366
    Key: 1 - Monday, 2 - Tuesday, 3 - Wednesday, 4 - Thursday, 5 - Friday
    6 - Saturday, 7 - Sunday.
    A non-leap year, has 52 weeks + 1 day.
    A leap year has 52 weeks + 2 days.
    """
    
    initialcalendar = (1,1,1900)
    initialcalendarday = 1
    startingcalendar = (startingday, startingmonth,startingyear)
    endcalendar = (endday, endmonth, endyear)
##    print(startingcalendar, endcalendar)
    a = daysElapsed(dayoftheweek, dayofthemonth, startingcalendar)
    b = daysElapsed(dayoftheweek, dayofthemonth, endcalendar)
    print(b,a,b-a)

    

def daysElapsed(dayoftheweek,dayofthemonth,date):
    day = date[0]
    month = date[1]
    year  = date[2]
    initialcalendar = (1,1,1900)
    initialcalendarday = 1
##    print(day,month,year,date)

    yearspassed = year - initialcalendar[2]
    monthspassed = month - initialcalendar[1]
    dayspassed = day - initialcalendar[0]
    monthsdays = {0:0, 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8: 31, 9:30,
                  10:31, 11:30, 12:31}
##    print("here",dayspassed)
##    from monthspassed to days passed:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        monthsdays[2] = 29
    else:
        monthsdays[2] = 28
    for i in range(0, monthspassed + 1):
        dayspassed += monthsdays[i]
##  from yearspassed to days passed:
    for i in range(initialcalendar[2],year):
        if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
            daysperyear = 366
        elif (initialcalendar[2]-year) == 0:
            pass
        else:
            daysperyear = 365
        dayspassed += daysperyear

##    print(dayspassed)


    WEEKDAYS = [1,2,3,4,5,6,7]

    countdaymonth = 1
    countday = 1
    countmonth = 1
    yearcount = 1900
    hits = 0
    for m in range(1, dayspassed+1):
        if yearcount % 400 == 0 or (yearcount % 4 == 0 and yearcount % 100 != 0):
            monthsdays[2] = 29
        else:
            monthsdays[2] = 28

##        print("a", "week", countday, dayoftheweek,"month", countdaymonth,dayofthemonth, countmonth,yearcount,m)
        if countday == dayoftheweek and countdaymonth == dayofthemonth:
            hits +=1
##            print("hurray",countday, countdaymonth,m)
        countday += 1
        countdaymonth +=1
##        print("b", countday,countdaymonth,countmonth,yearcount,m)
##        input()
        ## reset the week counter:
        
        if countday > len(WEEKDAYS):
            countday = 1
        if countdaymonth > monthsdays[countmonth]:
            countdaymonth = 1
            countmonth += 1
        if countmonth > 12:
            countmonth = 1
            yearcount +=1

    return hits
        
        
                
## The neat way of doing this:
##    import datetime
##    count = 0
##    for y in range(1901,2001):
##        for m in range(1,13):
##            if datetime.datetime(y,m,1).weekday() == 6:
##                count += 1
##    print(count)
       
def amicableNumbers(maxnumber):
    amicables = []
    trynumbers  = []
    for i in range(1, maxnumber+1):
        trynumbers.append(i)

    for i in trynumbers:

        za = zb = 0
        ax = calculatedivisorsnotconsecutive(i)
        try:
            ax.remove(i)
        except:
            pass
        za = sum(ax)
##        print("hola", i, za)
        bx = calculatedivisorsnotconsecutive(za)
##        print(bx, za)
        try:
            bx.remove(za)
        except:
            pass
        zb = sum(bx)
        if zb == i and i != za:
            amicables += [i,za]
            trynumbers.remove(i)
            trynumbers.remove(za)

##            print(amicables)

    amicables.sort()
    return amicables

def NamesScores(j,x):
    """ j is the index in the list, x is the word/name
    This returns the index+1 times the sum of the values of the letters
    """

    return (j+1) * (sum(ord(i)-64 for i in x))
    ## This is slightly faster than the alternative found on the forum,
    ## and MUCH faster than the original implementation using dictionaries to look up values:
    ##
    ##    x = eval( '[' + open( "F:\\VirtualBOX\\DropBox\\Dropbox\\python\\Euler\\problem_022_data.txt" ).readlines()[ 0 ] + ']' )
    ##    x.sort()
    ##
    ##    # Then calculate what is needed.
    ##
    ##    print(functools.reduce(lambda x, y: x + y, [functools.reduce(lambda x, y: x + y, [( j + 1 ) * (sum((ord( i ) - 64 ) for i in x[ j ]))]) for j in range(0, len( x ) ) ] ))

        ## Implementation with dictionaries.
        ##    letters = ["A", "B", "C", "D", "E", "F", "G",
        ##               "H", "I", "J", "K", "L", "M", "N",
        ##               "O", "P", "Q", "R", "S", "T", "U",
        ##               "V", "W", "X", "Y", "Z"]
        ##    lettervalue = dict(zip(letters,range(1,len(letters)+1)))
        ##
        ##
        ##    suma = 0
        ##    sumat = 0
        ##    dictnames = {}
        ##    map(NamesScores(listofnames),listofnames)
        ##    for a in listofnames:
        ##        x = 0
        ##        suma = 0
        ####        print(a)
        ##        map(NamesScores(a),a)
        ##        
        ##        for l in a:
        ##            try:
        ##                x += ord(l) - 64
        ##            except:
        ##                pass
        ##        suma += x*(listofnames.index(a)+1)
        ##        sumat += suma
        ##        dictnames[a] = [x, listofnames.index(a), suma]
        ##    print(sumat)


def abundantlist(start,end):
    """Returns a set of all the abundant numbers between start and end"""

    abundant = []
    for i in range(start,end+1):
        if i < sum(calculatedivisorsnotconsecutivenoself(i)):
            abundant.append(i)
  
    return abundant

def abundantset(start,end):
    """Returns a set of all the abundant numbers between start and end"""

    abundant = set()
    for i in range(start,end+1):
        if i < sum(calculatedivisorsnotconsecutivenoself(i)):
            abundant.add(i)
  
    return abundant



def euler23(Nmax):
    """ prints the sum of positive integers lower than Nmax that cannot be built as the sum of two abundant numbers"""
    # Calculate the set of abundantnumbers lower than Nmax.
    setofabs = abundantset(1,Nmax)
    # Set of integers that cannot be built by adding two abundant numbers.
    integerset = set()
    # Add integers to the set by recursively looking at the substraction of
    # the number and the items in the setofabs. If a coincidence is found, the
    # for loop breaks. If none is found, the integer is added to the set.
    for a in range(1,Nmax):
        doable = 0
        for j in setofabs:            
            if a - j in setofabs and a != a-j:
                doable = 1
                break
        if doable == 0:
            integerset.add(a)

    print(sum(integerset))
    print(len(integerset))   

def getpermutationlist(listn):
    import itertools
    return [x for x in itertools.permutations(listn)]

def euler24(listn,pos):
    a = getpermutationlist(listn)
    print(functools.reduce(lambda x,y: str(x) + str(y),[x for x in a[pos]]))

def euler25(lenmax):
    a = 1
    b = 1
    c = 0
    counter = 2
    while len(str(c)) < lenmax:
        c = a + b
        a = b
        b = c
        counter +=1
    print(counter)

def euler27(number):
    a = 0
    b = 0
    mx = 0
    total = 0
    summary = (a, b, mx, total)
    l = []
    dictm = {}
    for a in range(-number+1,number):
        for b in range(-number+1, number):
            if b == 500 and a != 0 and a%b == 0:
                print(a,b)
            summary = iter27(a,b)
            a, b, mx, total = summary
            b 
            if mx != 0:
                l.append((a,b,mx,total))
                dictm[mx] = (a,b)
    maxm, keys = [max(dictm.keys())],dictm[max(dictm.keys())]
    return maxm, keys 
            
            
def iter27(a,b):
    mx = 0
    total = 0
    summary = (a, b, mx, total)

    for i in itertools.count(0):
        m = i*i + i*a + b
        if m > 0 and m in primesfrom2to(m+1):
            mx = i
            summary = (a, b, mx, total)
        else:
            return summary
    

def main():
    start = time.time()
    
    maxm, keys = euler27(1000)
    print(maxm, keys)

                

    
    end = time.time()
    print(end -start)
    
    
    

    
main()
