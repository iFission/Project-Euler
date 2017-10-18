# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import sys
from time import time

if __name__ == '__main__':

	n = int(sys.argv[1])

	start = time()

	end = time()
	print (end - start, "milliseconds.")