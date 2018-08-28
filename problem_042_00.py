##The nth term of the sequence of triangle numbers is given by,
##tn = ½n(n+1); so the first ten triangle numbers are:
##
##1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
##
##By converting each letter in a word to a number corresponding
##to its alphabetical position and adding these values we form
##a word value. For example, the word value for SKY is
##19 + 11 + 25 = 55 = t10. If the word value is a triangle number
##then we shall call the word a triangle word.
##
##Using words.txt (right click and 'Save Link/Target As...'),
##a 16K text file containing nearly two-thousand common English words,
##how many are triangle words?


import numpy as np
import itertools
import math
import time

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

def triangles(maxval):
    """tn = ½n(n+1) 1, 3, 6, 10, 15, 21"""
    m = 0
    a = 1
    b = 1
    c = -2*maxval
    lt = set()
    upb = max((-b+math.sqrt(b*b-4*a*c))/2,(-b-math.sqrt(b*b-4*a*c))/2)
    for m in range(1,int(upb)+1):
        lt.add(0.5*m*(m+1))

    return lt

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
    
        
def euler42(filename):
    lw = convertfiletolist(filename)
    maxval = maxvalue(lw)
##    print(maxval)
    st = triangles(maxval)
##    print(st)
    print(evaluatelist(lw, st))

def main():
    start = time.time()
    euler42("words.txt")
##    print(evaluatelist(["SKY","REGIONAL"], triangles(1000)))
##    print(valueword("ABOUT"))
##    print(valueword("SKY"))
    end = time.time()
    print(end-start)


main()
