# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!


import sys
from time import time


from math import factorial
from functools import reduce
from operator import mul


def factorial_mul(n):
	return reduce(mul, range(1, n + 1))


def factorial_lambda(n):
	return reduce((lambda x,y: x * y), range(1, n + 1))


def sum_of_digits(n):
	return sum(map(int,list(str(n))))


if __name__ == '__main__':
	start = time()

	n = int(sys.argv[1])
	print(sum_of_digits(factorial(n)))

	end = time()
	print (end - start, "milliseconds.")


	start = time()

	n = int(sys.argv[1])
	print(sum_of_digits(factorial_mul(n)))

	end = time()
	print (end - start, "milliseconds.")


	start = time()

	n = int(sys.argv[1])
	print(sum_of_digits(factorial_lambda(n)))

	end = time()
	print (end - start, "milliseconds.")


# $ python3 20.py 100
# 648
# 0.00016307830810546875 milliseconds.
# 648
# 9.703636169433594e-05 milliseconds.
# 648
# 0.00012302398681640625 milliseconds.


# $ python3 20.py 100000
# 1938780
# 3.70434308052063 milliseconds.
# 1938780
# 7.148431777954102 milliseconds.
# 1938780
# 7.1153950691223145 milliseconds.