##Multiples of 3 and 5
##Problem 1
##If we list all the natural numbers below 10 that are multiples of 3 or 5,
##we get 3, 5, 6 and 9. The sum of these multiples is 23.
##
##Find the sum of all the multiples of 3 or 5 below 1000.

import numpy as np
import timeit

def calculate_m(Nmax,number1,number2):
        
    # create the array with all "False" values
    series_m = np.zeros(Nmax, dtype=bool)

    # Change to true when multiple of number1 or number2
    series_m[number1::number1] = True
    series_m[number2::number2] = True

    return series_m

def check_sum(Nmax, number1, number2):
    numbertar = calculate_m(Nmax, number1, number2)
    # identify indices and do the sum
    nz = np.nonzero(numbertar)
    return nz[0].sum()

def main():
    cs = check_sum(1000,3,5)
    print(cs)    
    print("timing...")
    t = timeit.Timer("check_sum(1000,3,5)", "from __main__ import calculate_m\nfrom __main__ import check_sum")
    print(t.timeit())
    print("job done")

main()

