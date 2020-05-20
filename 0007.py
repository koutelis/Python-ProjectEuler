# PROBLEM 7 - 10001st prime
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import math

target = 10001
counter = 1
number = 2

while True:
    if all(number%i!=0 for i in range(2,int(math.sqrt(number))+1)):
        if counter == target:
            print(number)
            break
        counter += 1
    number += 1