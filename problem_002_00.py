##Even Fibonacci numbers
##Problem 2
##Each new term in the Fibonacci sequence is generated by adding the previous
##two terms. By starting with 1 and 2, the first 10 terms will be:
##
##1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
##
##By considering the terms in the Fibonacci sequence whose
##values do not exceed four million, find the sum of the
##even-valued terms.

import numpy as np
import timeit

def calculate_f(Nmax):
    listfibo = [2]
    n1 = 1
    n2 = 2
    n = 0
    while n < Nmax:
        n = n1 + n2
        n1 = n2
        n2 = n
        if n <= Nmax and n%2 == 0:
            listfibo.append(n)

    return listfibo

##def check_sum(Nmax, number1, number2):
##    numbertar = calculate_m(Nmax, number1, number2)
##    # identify indices and do the sum
##    nz = np.nonzero(numbertar)
##    return nz[0].sum()

def main():
    cs = calculate_f(4000000)
    print(cs)
    print(sum(cs))
##    print("timing...")
##    t = timeit.Timer("check_sum(1000,3,5)", "from __main__ import calculate_m\nfrom __main__ import check_sum")
##    print(t.timeit())
##    print("job done")

main()

