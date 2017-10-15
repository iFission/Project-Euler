# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import sys
from time import time

# implementation using objects
class ss(object):
	"""docstring for ss"""
	def __init__(self, n):
		super(ss, self).__init__()
		self.n = n

	def sum_square(self):
		sum = 0
		for i in range(1, self.n + 1):
			sum += i ** 2
		return sum

	def square_sum(self):
		sum = 0
		for i in range(1, self.n + 1):
			sum += i
		return sum ** 2

	def diff(self):
		print(self.square_sum() - self.sum_square())
		return

# normal implementation
def sum_square(n):
	sum = 0
	for i in range(1, n + 1):
		sum += i ** 2
	return sum

def square_sum(n):
	sum = 0
	for i in range(1, n + 1):
		sum += i
	return sum ** 2

def diff(n):
	print(square_sum(n) - sum_square(n))
	return
if __name__ == '__main__':

	n = int(sys.argv[1])

	start = time()
	ss(n).diff()
	end = time()
	print (end - start, "milliseconds.")

	start = time()
	diff(n)
	end = time()
	print (end - start, "milliseconds.")

# overall normal implementation faster than object implementation
# $ python3 6.py 100
# 25164150
# 6.198883056640625e-05 milliseconds.
# 25164150
# 5.030632019042969e-05 milliseconds.