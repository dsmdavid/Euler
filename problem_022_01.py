##Names scores
##Problem 22
##Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
##containing over five-thousand first names, begin by sorting it into alphabetical order.
##Then working out the alphabetical value for each name, multiply this value by its alphabetical
##position in the list to obtain a name score.
##
##For example, when the list is sorted into alphabetical order, COLIN,
##which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
##So, COLIN would obtain a score of 938  53 = 49714.
##
##What is the total of all the name scores in the file?
##


import numpy as np
import time
import functools


def readfromfilesamplenames(filename):

    fo = open(filename,"r")
    list1 =[]
    for line in fo:
        list1.append(line.replace("\n", "").replace('"',"").split(","))
    fo.close()

    return list1[0]

def NamesScores(j,x):
    """ j is the index in the list, x is the word/name
    This returns the index+1 times the sum of the values of the letters
    """

    return (j+1) * (sum(ord(i)-64 for i in x))
    ## This is slightly faster than the alternative found on the forum,
    ## and MUCH faster than the original implementation using dictionaries to look up values:
    ##
    ##    x = eval( '[' + open( "F:\\VirtualBOX\\DropBox\\Dropbox\\python\\Euler\\problem_022_data.txt" ).readlines()[ 0 ] + ']' )
    ##    x.sort()
    ##
    ##    # Then calculate what is needed.
    ##
    ##    print(functools.reduce(lambda x, y: x + y, [functools.reduce(lambda x, y: x + y, [( j + 1 ) * (sum((ord( i ) - 64 ) for i in x[ j ]))]) for j in range(0, len( x ) ) ] ))


def main():
    start = time.time()
    
    listofnames = sorted(readfromfilesamplenames("F:\\VirtualBOX\\DropBox\\Dropbox\\python\\Euler\\problem_022_data.txt"))
    

    ## Two alternatives, approx. the same time:
    ## verbose
    a = 0
    for i in range(0,len(listofnames)):
        a += NamesScores(i,listofnames[i])
    print(a)
    ## Compact:
    ##    print(functools.reduce(lambda x,y: x+y, [NamesScores(i,listofnames[i]) for i in range(0, len(listofnames))]))

    end = time.time()
    print(end -start)
    
main()
