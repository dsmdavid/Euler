
##Triangular, pentagonal, and hexagonal
##Problem 45
##Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
##
##Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
##Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
##Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
##It can be verified that T285 = P165 = H143 = 40755.
##
##Find the next triangle number that is also pentagonal and hexagonal.

import numpy as np
import itertools
import math
import time
import eulertools as et


def isTriangle(number):
    _tmp = 0
    _conditionplus = (-1 + np.sqrt(1 + 8*number))/2
    if int(_conditionplus) == _conditionplus:
        _tmp = 1

    return _tmp

def isPentagonal(number):
    _tmp = 0
    _conditionplus = (1+np.sqrt(1+24*number))/6
    if int(_conditionplus) == _conditionplus:
        _tmp = 1

    return _tmp

def isHexagonal(number):
    _tmp = 0
    _conditionplus = (1+np.sqrt(1+8*number))/4
    if int(_conditionplus) == _conditionplus:
        _tmp = 1

    return _tmp


def createpent(n):
    pn = n * (3 * n - 1) / 2
    return pn

def createHex(n):
    hn = n * (2 * n -1)
    return hn



## 1. Find the first couple of pentagonal numbers whose difference is also
## a pentagonal number.
## 1.a. Create a list of pentagonal numbers.
## 1.b. Create the next pentagonal number.
## 1.c. Test if the new pentagonal number, minus any of the pentagonal numbers
## in the list yields a pentagonal number, if so, add it to a set of combinations.
def euler45b():
    n = 40755
    flag = True
    while flag == True:
        n +=1
        m = createHex(n)
        if isPentagonal(m):
            if isTriangle(m):
                print(m)
                flag = False

def euler45():
    n = 40755
    flag = True
    while flag == True:
        n += 1
        if isHexagonal(n):
            if isPentagonal(n):
                if isTriangle(n):
                    print(n)
                    flag = False
    
##    setpent = set()
##    listpent = set()
##    listdif = []
##    dictdif = {}
##    proceed = 1
##    current_n = 1
##    while proceed == 1:
##        #1.b
##        pn = createpent(current_n)
##        listpent.add(pn)
####        print(listpent)
####        input("a")
##        #1.c
####        print(current_n)
####        if pn == 92:
####            input(92)
##        for i in listpent:
####            print(i)
##            try:
##                dif = pn - i
##                
####                print("dif " + str(dif))
##                if dif in listpent:
####                    print(dif,pn,i,current_n)
####                    sv = frozenset[pn, i, dif]
####                    print(sv)
##                    if isPentagonal(pn+i) != 3:
####                            setpent.add(sv)
####                            print(setpent)
##                        print(dif, pn, i)
####                        input("b " + str(current_n))
##                        proceed = 0
##                else:
##                    pass
##            except:
##                pass
##        current_n += 1
####        if current_n % 1000 == 0:
####            print(current_n)
####        input("c " + str(current_n))
####        listpent
####        input("listpent")
##        
##        #print(current_n, listpent)
##
    



##def convertfiletolist(filename):
##    f = open(filename)
##    lw = f.read().replace('"',"").split(",")
##    f.close()
##    return lw
##
##def maxvalue(listw):
##    maxl = 0
##    maxv = ord("Z") - 64
##    for i in listw:
##        maxl = max(maxl, len(i))
##    return maxl*maxv
##
##def valueword(word):
##    value = 0
##    for i in word:
##        value += ord(i)
##    value = value -(64*len(word))
####    print("value = ", value, end = " ")
##    return value
##
##def evaluatelist(lw,st):
##    count = 0
##    for i in lw:
####        print(i, end = " ")
##        vw = valueword(i)
####        print(vw, end = "\n")
##        if vw in st:
##            count +=1
####            print("new", i, vw, "\n")
##    return count
##    
##def evaluaten(n,lp):
##    sn = str(n)
##    c = 0
##    d = 0
##    for i in range(2,9):
##        if int(sn[i-1:i+2]) % lp[d] == 0:
##            c += 0
##        else:
##            c += 1
##        d += 1
##        
##    if c == 0: return True
##    else: return False
##        
##def euler43():
##    """Generates listofprimes < 18, evaluates permutations 0-9 for Euler43"""
##    
##    lp = et.primesfrom2to(18)
##    print(lp)
##    s = ""
##    for x in range(0,10):
##        s += str(x)
##
##
##
##    listes=[]
##    lv = []
##    for n in itertools.permutations(s):
##        sn = createseq(n)
##        if evaluaten(sn,lp):
##            listes.append(int(sn))
##
##    
##    print(sum(listes))
##    print(listes[1])
##    print(evaluate(str(listes[1]),lp))
##
####
####print(evaluaten("1406357289",et.primesfrom2to(18)))
####input("result")



def main():
    start = time.time()
    euler45b()
##    print(evaluatelist(["SKY","REGIONAL"], triangles(1000)))
##    print(valueword("ABOUT"))
##    print(valueword("SKY"))
    end = time.time()
    print(end-start)


main()