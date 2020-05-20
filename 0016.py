#PROBLEM 16 – Power digit sum
"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

n = 15
total = 0

for num in str(2**n):
    total += int(num)

print(total)
