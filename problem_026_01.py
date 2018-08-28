##A unit fraction contains 1 in the numerator. The decimal representation
##of the unit fractions with denominators 2 to 10 are given:
##
##1/2	= 	0.5
##1/3	= 	0.(3)
##1/4	= 	0.25
##1/5	= 	0.2
##1/6	= 	0.1(6)
##1/7	= 	0.(142857)
##1/8	= 	0.125
##1/9	= 	0.(1)
##1/10	= 	0.1
##Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
##It can be seen that 1/7 has a 6-digit recurring cycle.
##
##Find the value of d < 1000 for which 1/d contains
##the longest recurring cycle in its decimal fraction part.
   
import numpy as np
import time
import functools
import math



def unitfraction(number):
    return float((1/number))

def recurring(number):
    #Convert to text the decimal part, after the decimal point, using
    #"Decimal", 53 decimals.
    from decimal import Decimal
    number = Decimal(number)
    decimalpart = str(number)[2:]
    l0 = [c for c in decimalpart]
    return l0

def checkrepetition(orderedlist):
    l0 = orderedlist[:]
    repetitionlist = []
    for k in range(0, len(l0)-1):
        # makes a second list starting in the next element.
        l1 = l0[k+1:]
##        print(l1)
        # checks if the element(k) in L0 is repeated.
        if l0[k] in l1:
            # finds the position at which the element is repeated
            ind1 = l1.index(l0[k])
##            print(ind1)
            # and modifies the list so that it starts in the repeated element.
            l1 = l1[ind1:]
            a = k
            b = 0
            seq = ""
##            print("l0[k] ", l0[k], " l1 ", l1, " l1[b] ", l1[b])
            while l0[a] == l1[b] and b < (len(l1)-1):
##                print("seq", seq)

                seq += l0[a]
                a += 1
                b += 1
##                print("seq += l0[a]", seq)

            if len(seq) > 1 and (seq[0] != seq[1]):
                repetitionlist.append(seq)
    value = 0
####    print("RL ", repetitionlist)
##    input()
    
    for element in repetitionlist:
        element, perelement = periodicity(element)
        if perelement > value:
##            print("value < perelement",value, perelement)
            value = perelement
##    print("printing list and value ", l0, value)
    return value
                
def periodicity(string):
    s = string
    k = len(s)
    l = []
    
    for n in range(0,k-1):
        if n != 0 and s[0] == s[n] and s[1] == s[n+1]:
            l.append(n)
##            print("periodicity", s, n)
    try:
        number = min(l)
    except:
        number = 0
##    print(s,number)
##    input()
    return s, number
                
def test26(number):
##    print("0 ",number)
    v = unitfraction(number)
##    print("1 ", v)
    l = recurring(v)
##    print("2 ", l)
    v = checkrepetition(l)
##    print("3 ", v)
    return number, v

def test26b(number):
    r = -1
    counter = 0
    divnumb = 10
    while r != 1:
        if counter > 1000:
            return number, 0
        if r == 0:
            return number, 0
        else:
            counter += 1
            if r == divnumb % number:
##                print(number, r, end = " ")
##                print(r, divnumb, counter)

                return number, counter
            else:

                r = divnumb % number
                divnumb *= 10
                
##    print(number, r, end = " ")
##    print(r, divnumb, counter)


    return number, counter        
            
def test26c(number):
    length,i = max((recur_len(i),i) for i in range(2,number))
    return length, i

import itertools
def recur_len(n):
    # digits for unit fraction 1/n
    r = 10 # initial remainder (10/n)/10
    seen = {} # remainder -> first pos
    for i in itertools.count(0):
        if r == 0:
            return 0  # divides evenly.
        elif r in seen:
            return i-seen[r] # curpos - firstpos
        seen[r] = i
        r= 10*(r % n)


        
        
        

##    
##send n to 1/n and return value
##send value to a function to evaluate the recurring cycle
##evaluate the presence of recurring cycle:
##    for each combination 
##compare the length of the recurring cycle with previous max length, replace 
def euler26(number):
    listofnumbers = [n for n in range(1,number)]
    dictn = {}
    maxdecimal = 0
    for n in listofnumbers:
        x, y = test26(n)
        dictn[y] = x
        if y > maxdecimal:
            maxdecimal = y

    print(maxdecimal, dictn[maxdecimal])
    print(dictn)

def euler26b(number):
    listofnumbers = [n for n in range(1,number)]
    dictn = {}
    maxdecimal = 0
    for n in listofnumbers:
        x, y = test26b(n)
        dictn[y] = x
        if y > maxdecimal:
            maxdecimal = y

    print(maxdecimal, dictn[maxdecimal])
##    print(dictn)
def euler26c(number):
    a, b = test26c(number)
    print(a,b)

    
def main():
    start = time.time()
    euler26c(1000)
    end = time.time()
    print("\nTime elapsed\t", end -start)
    
    
    

    
main()
