# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?


# solve using nCr method
# from (0, 0) to (n, k)
# number of Down (D) and (R) is the same
# order of D determines the order of R
# number of ways to arrange 20 R in 40 slots


import sys
from time import time
import scipy.special


def nCr(x, y):
	return int(scipy.special.binom(x + y, y))


if __name__ == '__main__':
	start = time()

	n = int(sys.argv[1])
	print(nCr(n, n))

	end = time()
	print (end - start, "milliseconds.")


# $ python3 15.py 20
# 137846528820
# 4.7206878662109375e-05 milliseconds.