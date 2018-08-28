##The number, 1406357289, is a 0 to 9 pandigital number because it is
##made up of each of the digits 0 to 9 in some order,
##but it also has a rather interesting sub-string divisibility property.
##
##Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
##
##d2d3d4=406 is divisible by 2
##d3d4d5=063 is divisible by 3
##d4d5d6=635 is divisible by 5
##d5d6d7=357 is divisible by 7
##d6d7d8=572 is divisible by 11
##d7d8d9=728 is divisible by 13
##d8d9d10=289 is divisible by 17
##Find the sum of all 0 to 9 pandigital numbers with this property.

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
