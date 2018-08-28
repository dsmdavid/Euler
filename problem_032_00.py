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

def pandigital(n1,n2,n3, N, listnumber):
    seq = str(n1)+str(n2)+str(n3)
    if len(seq) != N: return False
    c = 0
    for i in listnumber:
        if i not in seq:
            return False
    return True

    
##def test31():
##    9 ciphers.
##    1, 4, 4
##    2, 2, 5
##    1, 3, 5
    

def euler31():
    listnumber = [str(x) for x in range(1, 10)]
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
            if pandigital(n1,n2,n3, N, listnumber):
                st.add(n3)
##    print(st)
    sum_st = 0
    for i in st:
        sum_st += i
    print(sum_st)
    



def main():
    start = time.time()
    euler31()


    end = time.time()

    print(end-start, " time")


main()
