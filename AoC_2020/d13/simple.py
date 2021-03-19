'''
import numpy as np

arr = np.array([17,13])

x = np.lcm.reduce(arr)

print(x)

import math

def get_prime_factors(number):
    # https://medium.com/nerd-for-tech/prime-factorization-of-a-number-in-python-and-why-we-check-upto-the-square-root-of-the-number-111de56541f
    prime_factors = []

    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number / i

    if number > 2:
        prime_factors.append(int(number))

    return prime_factors


print(get_prime_factors(17))
print(get_prime_factors(13))
print(get_prime_factors(19))
# [2, 2, 3, 7]
'''

from functools import reduce
def chinese_remainder(n, a):
    sum=0
    prod=reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p=prod/n_i
        sum += a_i* mul_inv(p, n_i)*p
    return sum % prod
def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=a// b
        a, b= b, a%b
        x0, x1=x1 -q *x0, x0
    if x1<0 : x1+= b0
    return x1
n=[17,13,19]
a=[2,3,2]
print(chinese_remainder(n,a))
23.0