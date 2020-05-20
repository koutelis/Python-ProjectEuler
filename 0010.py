# PROBLEM 8 - Summation of primes
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math

target = 2000000
prime_sum = 0

for number in range(2, target):
    if all(number%i!=0 for i in range(2,int(math.sqrt(number))+1)):
        prime_sum += number

print(prime_sum)
