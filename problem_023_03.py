import time
import math

def sum_divisors(num):
    a = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            a += i
            if num / i != i:
                a += num/i
    return a

def gen_abundant(max):
    num = 11
    while 1:
        num += 1
        if num > max: raise StopIteration
        if sum_divisors(num) > num:
             yield num

t0 = time.time()
a = set(gen_abundant(28123))
b = set(num + num2 for num in a for num2 in a if num + num2 < 28124)
print(sum(range(28124)) - sum(b))
print(time.time()-t0)
