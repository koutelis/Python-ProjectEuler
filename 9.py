# PROBLEM 9 – SPECIAL PYTHAGOREAN TRIPLET
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

n = 1000

for c in range(2, n + 1):
    for b in range(1, n):
        if b >= c:
            break
        for a in range(n):
            if a >= b:
                break
            if (a + b + c == n) and (a**2 + b**2 == c**2) and (a < b < c):
                print(a*b*c)
