# PROBLEM 23 - Non-abundant sums
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number 
that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def abundant_gen(upper_limit):
	"""generates abundant numbers"""
	for num in range(upper_limit):
		if proper_divisors_sum(num) > num:
			yield num

def proper_divisors_sum(number):
	"""creates list of proper divisors for a number"""
	x = [divisor for divisor in range(1, number) if number % divisor == 0]
	return sum(x)


target = 28123

abundant_list = set([num for num in abundant_gen(target)])

abundant_sums = set()
for num1 in abundant_list:
	for num2 in abundant_list:
		abundant_sum = num1 + num2
		if abundant_sum > target:
			break
		abundant_sums.add(abundant_sum)

total = 0
for num in range(target):
	if num not in abundant_sums:
		total += num

print(total)
