##Pentagonal numbers are generated by the formula,
##Pn=n(3n−1)/2. The first ten pentagonal numbers are:
##
##1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
##
##It can be seen that P4 + P7 = 22 + 70 = 92 = P8.
##However, their difference, 70 − 22 = 48, is not pentagonal.
##
##Find the pair of pentagonal numbers, Pj and Pk,
##for which their sum and difference are pentagonal and
##D = |Pk − Pj| is minimised; what is the value of D?


import numpy as np
import itertools
import math
import time
import eulertools as et

def createseq(tupleseq):
    seq = ""
    for i in tupleseq:
        seq += i
    return seq

def isPentagonal(number):
    """Returns a tuple (a,b): a = 1, if there is a number (n) that satisfies
    number = n*(3n-1)/2 and 0 otherwise. b = the value of n that verifies that
    condition, 0 otherwise. """
    conditionplus = (1+np.sqrt(1+24*number))/2
    conditionminus = (1-np.sqrt(1+24*number))/2
    
    if int(conditionplus) == conditionplus:
        pass

    elif int(conditionminus) == conditionminus:
        pass

    else:
        pass

    return (a,b)

def convertfiletolist(filename):
    f = open(filename)
    lw = f.read().replace('"',"").split(",")
    f.close()
    return lw

def maxvalue(listw):
    maxl = 0
    maxv = ord("Z") - 64
    for i in listw:
        maxl = max(maxl, len(i))
    return maxl*maxv

def valueword(word):
    value = 0
    for i in word:
        value += ord(i)
    value = value -(64*len(word))
##    print("value = ", value, end = " ")
    return value

def evaluatelist(lw,st):
    count = 0
    for i in lw:
##        print(i, end = " ")
        vw = valueword(i)
##        print(vw, end = "\n")
        if vw in st:
            count +=1
##            print("new", i, vw, "\n")
    return count
    
def evaluaten(n,lp):
    sn = str(n)
    c = 0
    d = 0
    for i in range(2,9):
        if int(sn[i-1:i+2]) % lp[d] == 0:
            c += 0
        else:
            c += 1
        d += 1
        
    if c == 0: return True
    else: return False
        
def euler43():
    """Generates listofprimes < 18, evaluates permutations 0-9 for Euler43"""
    
    lp = et.primesfrom2to(18)
    print(lp)
    s = ""
    for x in range(0,10):
        s += str(x)



    listes=[]
    lv = []
    for n in itertools.permutations(s):
        sn = createseq(n)
        if evaluaten(sn,lp):
            listes.append(int(sn))

    
    print(sum(listes))
    print(listes[1])
    print(evaluate(str(listes[1]),lp))

##
##print(evaluaten("1406357289",et.primesfrom2to(18)))
##input("result")



def main():
    start = time.time()
    euler43()
##    print(evaluatelist(["SKY","REGIONAL"], triangles(1000)))
##    print(valueword("ABOUT"))
##    print(valueword("SKY"))
    end = time.time()
    print(end-start)


main()
