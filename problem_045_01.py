
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

def createTri(n):
    return n * (n + 1) / 2

def createPent(n):
    return n * (3 * n - 1) / 2
    

def createHex(n):
    return n * (2 * n -1)


def euler45b():

    
    n = 143
    flag = True
    while flag == True:
        n +=1
        m = createHex(n)
        if isPentagonal(m):
            if isTriangle(m):
                print(m)
                flag = False



def main():
    start = time.time()
    euler45b()
##    print(evaluatelist(["SKY","REGIONAL"], triangles(1000)))
##    print(valueword("ABOUT"))
##    print(valueword("SKY"))
    end = time.time()
    print(end-start)


main()