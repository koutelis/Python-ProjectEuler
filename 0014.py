# PROBLEM 14 - Longest Collatz sequence

"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatz(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + collatz(n / 2)
    else:
        return 1 + collatz(3 * n + 1)

target = 1000000
max_collatz = 0

for i in range(1, target):
    test = collatz(i)
    if test > max_collatz:
        max_collatz = test
        starting_num = i
   
print(f'max starting number: {starting_num} with {max_collatz} as the longest number chain')
