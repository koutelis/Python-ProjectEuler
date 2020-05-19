#PROBLEM 20 – Factorial digit sum
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factorial(num):
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product

def digit_sum(num):
    num = str(num)
    sum = 0
    for digit in num:
        sum += int(digit)
    return sum
    
    
x = 100
print(digit_sum(factorial(x)))
