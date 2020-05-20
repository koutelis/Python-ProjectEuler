# PROBLEM 4 - Largest palindrome product
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def palindrome_check(number):
    number = str(number)
    number_inv = number[::-1]
    half = len(number) // 2
    if number[:half] == number_inv[:half]:
        return int(number)

numlist = []
for x in range(999,0,-1):
    for y in range(999,0,-1):
        if palindrome_check(x * y):
            numlist.append(x * y)
            break
            
print(max(numlist))
