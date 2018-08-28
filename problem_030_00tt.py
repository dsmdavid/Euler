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




valmax = 2
COINVALUE = {"1p":0.01, "2p":0.02, "5p":0.05, "10p": 0.10,
		"20p":0.20, "50p":0.50, "1P":1, "2P":2}

potcomb = set()

####k = iterator.COINVALUE.keys()
##b = k
##
a, b, c, d, e, f, g, h = [x for x in COINVALUE.keys()]
##for i in range(0,len(vals)):
    
for n1pi in range(0, (valmax/COINVALUE[a])+1):
    newval = n1pi * COINVALUE[a]
    for n2pi in range(0, (valmax/COINVALUE[b])+1):
        newval += n2pi * COINVALUE[b]
        for n5pi in range(0, (valmax/COINVALUE[c])+1):
            if True:
                if True:
                    if True:
                        newval += n5pi * COINVALUE[c]
            
			for n10pi in range(0, (valmax/COINVALUE[d])+1):
                            if True:
                                newval += n10pi * COINVALUE[d]
                                for n20pi in range(0, (valmax/COINVALUE[e])+1):
                                    newval += n20pi * COINVALUE[e]
                                    for n50pi in range(0, (valmax/COINVALUE[f])+1):
                                        newval += n50pi * COINVALUE[f]
                                        for 1Pi in range(0, (valmax/COINVALUE[g])+1):
                                            newval += n1Pi * COINVALUE[g]
                                            for n2Pi in range(0, (valmax/COINVALUE[h])+1):
                                                newval += n2Pi * COINVALUE[h]
                                                if newval == 2:
                                                    combination = (1pi " 1p", 2pi " 2p", 5pi " 5p", 10pi " 10p",                                                                   20pi " 20p", 50pi " 50p", 1P " 1P", 2P " 2P")
                                                potcomb.add(combination)
print(len(potcomb))

##def test(astr):
##	v = valmax/COINVALUE[astr]
##	for n in range(0, v+1):
##		nv = n*COINVALUE[astr]
##		return nv
##
##l = COINVALUE.keys()[:]
##for a in range(len(COINVALUE.keys())):
##	b = pop(l)
##
##	a
##COINVALUE = {"1p":0.01,"2p":0.02,"5p":0.05,
##             "10p":0.10,"20p":0.20,"50p":0.50,
##             "1P":1.00,"2P":2.00}


             
def euler28(size):
    """Generates a spiral within a square of -number- side"""
    spire = np.zeros((size, size)) 
    print(spire)
    n = 0
    l = []
    for i in spire:
        for j in i:
            n += 1
            l.append(n)
    direction = ""
    last_position = ""
    for element in l:
##        print("here", size,element,spire, direction)
        spire, direction, new_position = move(size,element,last_position,spire, direction)
##        print(direction, new_position)
        print("new\n", spire)
        last_position = new_position
    print("END SPIRE:\n\n\n", spire)
    a = np.trace(spire) + np.trace(spire[::-1]) - 1
    print("Sum of diagonals = ", a)
    

def move(size,number,last_position, spire, direction):
    if number == 1:
##        print("inside move, number == 1")
        i = size//2
        j = size//2
        spire[i][j] = number
        direction = "E"
        new_position = (i, j)
        return spire, direction,new_position
##        return spire, new_position

    else:
##        print("inside else, ", number, direction, last_position)

        #move following direction, then check direction.
        if direction == "N":
            i = last_position[0] - 1
            j = last_position[1]
        elif direction == "E":
            i = last_position[0]
            j = last_position[1] + 1
        elif direction == "S":
            i = last_position[0] + 1
            j = last_position[1]
        elif direction == "W":
##            print("inside W")
            i = last_position[0]
            j = last_position[1] - 1
        else:
            print("Else, ", direction, last_position)
            print("Something went very wrong")
        spire[i][j] = number
        new_position = (i, j)
        direction = checkdirection(new_position, spire, direction)
    return spire, direction, new_position
            

def checkdirection(curr_pos, spire, curr_direction):
    directions = ("N", "E", "S", "W")
    i = curr_pos[0]
    j = curr_pos[1]
    new_dir = curr_direction
    
    if curr_direction == "N" and spire[i][j+1] == 0:
        new_dir = "E"
        return new_dir
    elif curr_direction == "E" and spire[i+1][j] == 0:
        new_dir = "S"
        return new_dir
    elif curr_direction == "S" and spire[i][j-1] == 0:
        return "W"
    elif curr_direction == "W" and spire[i-1][j] == 0:
        return "N"
    else:
        return new_dir
        
        
def euler30(n):
    numbers = []
##    itertools.count
    for i in range(2,354294):
        c = expon(i,n)
##        print(i,c)
        if c == i:
            numbers.append(i)
    print(sum(numbers))

def expon(N, n):
    a = str(N)
    b = 0
    for i in a:
        b += int(i)**n
##        print(i, a, b)
    return b

def main():
    start = time.time()
    
    euler28(7)

                

    
    end = time.time()
    print(end -start)
    
    
    

    
main()
