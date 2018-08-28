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

####k = iterator.COINVALUE.keys()
##b = k
##
##a, b, c, d, e, f, g, h = "1p", "2p", "5p", "10p","20p", "50p", "1P", "2P"
####for i in range(0,len(vals)):
##print(a,b,c,d,e,f,g,h)

def testb(valmax):
    a, b, c, d, e, f, g, h = "1p", "2p", "5p", "10p","20p", "50p", "1P", "2P"
    print(a,b,c,d,e,f,g,h)

    for n1pi in range(0, int(valmax/COINVALUE[a])+1):
        for n2pi in range(0, int(valmax/COINVALUE[b])+1):
            for n5pi in range(0, int(valmax/COINVALUE[c])+1):
                for n10pi in range(0, int(valmax/COINVALUE[d])+1):
                    for n20pi in range(0, int(valmax/COINVALUE[e])+1):
                        for n50pi in range(0, int(valmax/COINVALUE[f])+1):
                            for n1Pi in range(0, int(valmax/COINVALUE[g])+1):
                                for n2Pi in range(0, int(valmax/COINVALUE[h])+1):
                                    newvala = n1pi * COINVALUE[a]
                                    newvalb = n2pi * COINVALUE[b]
                                    newvalc = n5pi * COINVALUE[c]
                                    newvald = n10pi * COINVALUE[d]
                                    newvale = n20pi * COINVALUE[e]
                                    newvalf = n50pi * COINVALUE[f]
                                    newvalg = n1Pi * COINVALUE[g]
                                    newvalh = n2Pi * COINVALUE[h]
                                    newval = newvala +newvalb+newvalc+newvald+newvale+newvalf+newvalg+newvalh
                                    combination = (str(n1pi) +" 1p", str(n2pi) + " 2p", str(n5pi) +" 5p",
                                                                               str(n10pi) +" 10p",  str(n20pi) +" 20p", str(n50pi) +" 50p",
                                                                               str(n1Pi) +" 1P", str(n2Pi) +" 2P")
##                                    print(newval, combination)
                                    if int(newval) == valmax:
##                                        print("hit found:")
##                                        print(combination)
##                                        input()
                                        potcomb.add(combination)
##    print(potcomb)
    print(len(potcomb))


def lh(valmax, current_value, coin, seq):    
    for n in range(0, int(valmax/COINVALUE[coin])+1):
        coin_number = n
        newvalue, combination = ch(current_value, coin, coin_number, seq)
##        if new_val == target:
##            if lastcoin:
##                end
##
##            else:
##                next lh
####        elif new_val < target:
####            next lh
####        elif new_val > target:
####            break
##
##    if  n == 0:
##        return 0
##    else:
##        return f((n-1))
##
##    if len(lc) = 1:
##        return a
##    else:
##        return b

##    for i in range(0, len(lc)):


def ch(current_value, coin, coin_number, seq):
    print("coin =", coin, "coin_number =", coin_number, "seq =",seq,"update\t", end = "\n")
    cn = coin_number
    valadd = cn * COINVALUE[coin]
    new_val = current_value + valadd
    print("\tcurrent_value= " , current_value ,"\tvaladd", valadd, "\tnewval =", new_val,"newseq = ", str(seq + str(cn) + " "+coin))
    return new_val, str(seq+"-" + str(cn) + " "+coin)
    
def testc(valmax):
    lc = ("1p", "2p", "5p", "10p","20p", "50p", "1P", "2P")
    a, b, c, d, e, f, g, h = [x for x in lc]
    print(a,b,c,d,e,f,g,h)
    
    val = 0
    count = 0
    seq =""
##    lh(valmax,val,lc[0], seq)
##    while len(lc) > 0:
##        x = pop(lc[0])
##        newvalue,seq = lh(valmax, val, x,seq)
        
    nv = 0
    for n1pi in range(0, int(valmax/COINVALUE[a])+1):
        val = 0
        seq =""

        coin_number = n1pi
        coin = a
        nv, seq = ch(val,coin, coin_number, seq)
        val = nv
        if int(val) < int(valmax + 1):
            for n2pi in range(0, int(valmax/COINVALUE[b])+1):
                coin_number = n2pi
                coin = b
                nv, seq = ch(val,coin, coin_number, seq)
                val = nv
                if int(val) < int(valmax + 1):
                    for n5pi in range(0, int(valmax/COINVALUE[c])+1):
                        coin_number = n5pi
                        coin = c
                        nv, seq = ch(val,coin, coin_number, seq)
                        val = nv
                        if int(val) < int(valmax + 1):
                            for n10pi in range(0, int(valmax/COINVALUE[d])+1):
                                coin_number = n10pi
                                coin = d
                                nv, seq = ch(val,coin, coin_number, seq)
                                val = nv
                                if int(val) < int(valmax + 1):
                                    for n20pi in range(0, int(valmax/COINVALUE[e])+1):
                                        coin_number = n20pi
                                        coin = e
                                        nv, seq = ch(val,coin, coin_number, seq)
                                        val = nv
                                        if int(val) < int(valmax + 1):
                                            for n50pi in range(0, int(valmax/COINVALUE[f])+1):
                                                coin_number = n50pi
                                                coin = f
                                                nv, seq = ch(val,coin, coin_number, seq)
                                                val = nv
                                                if int(val) < int(valmax + 1):
                                                    for n1Pi in range(0, int(valmax/COINVALUE[g])+1):
                                                        coin_number = n1Pi
                                                        coin = g
                                                        nv, seq = ch(val,coin, coin_number, seq)
                                                        val = nv
                                                        if int(val) < int(valmax + 1):
                                                            for n2Pi in range(0, int(valmax/COINVALUE[h])+1):
                                                                coin_number = n2Pi
                                                                coin = h
                                                                nv, seq = ch(val,coin, coin_number, seq)
                                                                val = nv
                                                                if int(val) == int(valmax):
                                                                    potcomb.add(seq)

    print(potcomb)
    print(len(potcomb))


def testd(target):
    lc = ("1p", "2p", "5p", "10p","20p", "50p", "1P", "2P")
    a, b, c, d, e, f, g, h = [x for x in lc]
    print(a,b,c,d,e,f,g,h)
    valarra=np.array([1,2,5,10,20,50,100,200])
    
    valmax = target
    for n1pi in range(0, int(valmax/COINVALUE[a])+1):
        testarr = np.zeros(8, dtype = int)
        for n2pi in range(0, int(valmax/COINVALUE[b])+1):
            for n5pi in range(0, int(valmax/COINVALUE[c])+1):
                for n10pi in range(0, int(valmax/COINVALUE[d])+1):
                    for n20pi in range(0, int(valmax/COINVALUE[e])+1):
                        for n50pi in range(0, int(valmax/COINVALUE[f])+1):
                            for n1Pi in range(0, int(valmax/COINVALUE[g])+1):
                                for n2Pi in range(0, int(valmax/COINVALUE[h])+1):
                                    testarr = np.array([n1pi,n2pi,n5pi,n10pi,n20pi,n50pi,n1Pi,n2Pi],dtype = int)
                                    check = testarr*valarra
                                    if check.sum() == target:
                                        combination = ""
                                        for x in range(0,len(lc)):
                                            combination += " "+ str(testarr[x])+"x"+ str(lc[x])
##                                        print(testarr)
##                                        print(combination)
                                        potcomb.add(combination)
                                        
##    print(potcomb)
    print(len(potcomb))
                                        
                                    

    
testd(200)
