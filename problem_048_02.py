##The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

##Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

import numpy as np
import itertools
import math
import time
import eulertools as et

def euler48(end):
    suma = 0
    for i in range(1,end+1):
        suma += i ** i
##        tmp_val = 1
####        print("i", i)
##
##        for j in range(1,i+1):
####            print("i ", i, "j ", j)
##            tmp_val = i * tmp_val
##            if len(str(tmp_val)) > 10:
####                break
##                tmp_val = int(str(tmp_val)[-11:])
####        print(i,j, tmp_val)
##        
##                
##
##        
##        suma += tmp_val
####        print(suma)
##        if len(str(suma)) > 12:
##            suma = int(str(suma)[-12:])
    print(str(suma)[-12:])

def main():
    start = time.time()
    euler48(1000)
    end = time.time()
    print(end-start)


main()
