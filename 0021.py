#PROBLEM 21 – Amicable numbers
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def proper_divisors(number):
    """returns list of divisors"""
    lst = []
    for i in range(1, number):
        if number % i == 0:
            lst.append(i)
    return lst

def has_amicable_pair(number):
	"""tests for amicable pairs"""
	x = sum(proper_divisors(number))
	y = sum(proper_divisors(x))
	if x != y:
		return y == number

amicable_pairs = []
for i in range(2, 10000):
	if has_amicable_pair(i):
		amicable_pairs.append(i)
		#print('amicable pair: {} and {}'.format(i, sum(proper_divisors(i))))

print(sum(amicable_pairs))
