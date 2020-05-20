# PROBLEM #6 – Sum square difference
"""
The sum of the squares of the first ten natural numbers is,

1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)^2=55^2=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def squared_then_sum(max_num):
    total = 0
    for num in range(1, max_num + 1):
        total += num**2
    return total

def sum_squared(max_num):
    total = 0
    for num in range(1, max_num + 1):
        total += num
    return total**2

n = 100

print(sum_squared(n) - squared_then_sum(n))
