# PROBLEM 5 - Smallest multiple
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
   
given_number = 20

numerator = given_number
while True:
    isDiv = True
    for divider in range(given_number // 2 + 1, given_number):
        if numerator % divider != 0:
            isDiv = False
            break
    if isDiv:
        print(numerator)
        break
    numerator += given_number
