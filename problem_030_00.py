##Starting with the number 1 and moving to the right
##in a clockwise direction a 5 by 5 spiral is formed
##as follows:
##
##21 22 23 24 25
##20  7  8  9 10
##19  6  1  2 11
##18  5  4  3 12
##17 16 15 14 13
##
##It can be verified that the sum of the numbers on the
##diagonals is 101.
##
##What is the sum of the numbers on the diagonals
##in a 1001 by 1001 spiral formed in the same way?
    
import numpy as np
import time
import functools
import math
import itertools

def euler28(size):
    """Generates a spiral within a square of -number- side"""
    spire = np.zeros((size, size)) 
##    print(spire)
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
##        print("new", spire)
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
    
    euler30(5)

                

    
    end = time.time()
    print(end -start)
    
    
    

    
main()
