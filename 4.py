# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


import sys
from time import time
from itertools import combinations_with_replacement as cwr


# print(list(itertools.combinations_with_replacement([n for n in range(3)], 2)))
# [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
# print(list(itertools.permutations([n for n in range(3)], 2)))
# [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
# print(list(itertools.combinations([n for n in range(2)], 2)))
# [(0, 1)]
# print(list(itertools.product([n for n in range(3)], repeat=2)))
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]


# product of m digits and n numbers, and step
# implemented using object model


# class for palindrome object, with methods for calculation
class Palindrome(object):
	"""docstring for palindrome"""
	def __init__(self, digit=1, numbers=1, step=1): # default values if not provided
		# self.digit = digit
		self.min = 10 ** (digit - 1)
		self.max = 10 ** digit - 1

	def compute(self):
		numbers_sets = cwr([n for n in range(self.max, self.min - 1, -1)], numbers) # min - 1 to print min # generates the sets of n numbers to be multiplied

		pal_number = 0
		for numbers_set in numbers_sets: # iterate the set of numbers
			product = 1
			for number in numbers_set:
				product *= number # finds the product of the n numbers in the set
				if self.check(product) and product > pal_number:
					pal_number = product
					PalSet = numbers_set
					print(pal_number)
				# print(product, set)
		print(pal_number, PalSet)
		return

	def reverse(self, number):
		return int(str(number)[::-1]) # reverses int using slice notation, [start:end:step]

	def reverse_alt(self, number): # alternate method to reverse int
		rev = 0
		temp = number
		while temp != 0:
			rev = rev * 10 + temp % 10 # increase rev by factor 10, then add the last digit of temp
			temp //= 10
		return rev

	def check(self, number):
		return number == self.reverse(number)


if __name__ == '__main__':
	start = time()

	digit, numbers, step = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
	# print(digit, numbers, step)
	# print(palindrome().reverse(10002)) # p.() to instantiate, else reverse will not have self argument
	Palindrome(digit, numbers, step).compute()

	end = time()
	print (end - start, "milliseconds.")


# $ python3 4.py 3 2 1
# 999
# 580085
# 906609
# 906609 (993, 913)
# 0.742830753326416 milliseconds.