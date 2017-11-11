# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

import sys
from time import time


if __name__ == '__main__':
	start = time()

	s = 0
	for n in range(1,1000):
		if n % 3 == 0 or n % 5 == 0:
			# print(n)
			s = s + n
	print(s)

	end = time()
	print (end - start, "milliseconds.")


# $ python3 1.py
# 233168
# 0.00019598007202148438 milliseconds.