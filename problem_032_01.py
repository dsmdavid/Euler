##a = b*c
##str(a)+str(b)+str(c) = pandigital(9)

import time
import numpy as np






def divisors(maxlimit):
    npdivisors = set()
    for i in range(2, int(maxlimit/2)+1):
        if maxlimit % i == 0:
            a = [int(i), int(maxlimit/i), int(maxlimit)]
            a.sort()
            b = (a[0],a[1],a[2])
            npdivisors.add(b)
    return npdivisors

def pandigital(n1,n2,n3, N):
    seq = set(str(n1)+str(n2)+str(n3))
    if "0" in seq: return False
    if len(seq) != N: return False
    return True

    
##def test31():
##    9 ciphers.
##    1, 4, 4
##    2, 2, 5
##    1, 3, 5
    

def euler32():
##    listnumber = [str(x) for x in range(1, 10)]
##    print(listnumber)
    N = 9
##    a = 7254
##    b = 39
##    c = 186
##    d = pandigital(a,b,c,N, listnumber)
##    print(d)
    st = set()
    for i in range(1000,9999):
        sd = divisors(i)
        for j in sd:
            n1, n2, n3 = j[0], j[1], j[2]
            if pandigital(n1,n2,n3, N):
                st.add(n3)
##    print(st)
    sum_st = 0
    for i in st:
        sum_st += i
    print(sum_st)
    
def euler32b():
    st = set()
    N = 9
    for i in range(11, 100):
        for j in range(i, 1000):
            p = i*j
            if pandigital(i,j,p, N): st.add(p)
    for i in range(0, 10):
        for j in range(1000, 10000):
            p = i*j
            if pandigital(i,j,p, N): st.add(p)

    sum_st = 0
    for i in st:
        sum_st += i
    print(sum_st)
    
            



def main():
    start = time.time()
    euler32b()


    end = time.time()

    print(end-start, " time")


main()
