##In England the currency is made up of pound, £, and pence, p,
##and there are eight coins in general circulation:
##
##1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
##It is possible to make £2 in the following way:
##
##1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
##How many different ways can £2 be made using any number of coins?
    
import numpy as np
import time
import functools
import math
import itertools




valmax = 5
COINVALUE = {"1p":1, "2p":2, "5p":5, "10p": 10,
		"20p":20, "50p":50, "1P":100, "2P":200}

potcomb = set()


def testb(valmax):
    counter = 0
    a,b,c,d,e,f,g,h = [0]*8
    for a in range(0, valmax+1):
        total = a
        for b in range(0, int((valmax-total)/2 + 1)):
            total = a + 2*b
            if a + 2*b > valmax: break
            for c in range(0, int((valmax-total)/5 + 1)):
                total = a + 2*b +5*c
                if a + 2*b +5*c  > valmax: break
                for d in range(0, int((valmax-total)/10 + 1)):
                    total = a + 2*b +5*c + 10*d
                    if a + 2*b +5*c +10*d > valmax: break
                    for e in range(0, int((valmax-total)/20 + 1)):
                        total = a + 2*b +5*c +10*d+20*e 
                        if a + 2*b +5*c +10*d+20*e > valmax: break
                        for f in range(0, int((valmax-total)/50 + 1)):
                            total = a + 2*b +5*c +10*d+20*e +50*f
                            if a + 2*b +5*c +10*d+20*e+50*f > valmax: break
                            for g in range(0, 3):
                                if a + 2*b +5*c +10*d+20*e+50*f+100*g > valmax: break
                                for h in range(0, 2):
                                    total = a + 2*b +5*c +10*d+20*e+50*f+100*g+200*h
                                    if total == valmax:
                                        counter += 1
                                    a,b,c,d,e,f,g,h = [0]*8
                                        

    print(counter)


def lh(valmax, current_value, coin, seq):    
    for n in range(0, int(valmax/COINVALUE[coin])+1):
        coin_number = n
        newvalue, combination = ch(current_value, coin, coin_number, seq)



def ch(current_value, coin, coin_number, seq):
    print("coin =", coin, "coin_number =", coin_number, "seq =",seq,"update\t", end = "\n")
    cn = coin_number
    valadd = cn * COINVALUE[coin]
    new_val = current_value + valadd
    print("\tcurrent_value= " , current_value ,"\tvaladd", valadd, "\tnewval =", new_val,"newseq = ", str(seq + str(cn) + " "+coin))
    return new_val, str(seq+"-" + str(cn) + " "+coin)
 

def validator(testarr):
    valarra=np.array([1,2,5,10,20,50,100,200])
    check = testarr*valarra
    return check.sum()

testb(40)
