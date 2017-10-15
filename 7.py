# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import sys
from time import time

if __name__ == '__main__':

	n = int(sys.argv[1])

	start = time()

	end = time()
	print (end - start, "milliseconds.")