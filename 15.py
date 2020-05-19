# PROBLEM 15 - Lattice paths

"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from math import factorial

n = 20

print(int(factorial(2 * n) / (factorial(n))**2))
