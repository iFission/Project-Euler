# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# product of m digits and n numbers

import sys

class palindrome(object):
	"""docstring for palindrome"""
	def __init__(self, digit):
		# self.digit = digit
		self.min = 10 ** (digit - 1)
		self.max = 10 ** digit - 1

	def pmin(self):
		print(self.min)

	def pmax(self):
		print(self.max)

	def compute(self):
		p1, p2, number = 0, 0, 0
		for n1 in range(self.max, self.min - 1, -1): # min - 1 to print min
			for n2 in range(self.max, self.min - 1, -1): # min - 1 to print min
				product = n1 * n2
				if self.check(product) and product > number:
					number = product
					p1 = n1
					p2 = n2
					print(number)
		print(p1, p2, number)

	def reverse(self, number):
		return int(str(number)[::-1])

	def check(self, number):
		return number == self.reverse(number)

if __name__ == '__main__':
	digit = int(sys.argv[1])
	p = palindrome(digit)
	p.compute()

	# print(p.min) # able to print as p.min is an int
