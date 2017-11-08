# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


import sys
import math
from time import time


def sum_check(a, b, c):
	return a + b + c == 1000

def gen_py_tri(max): # generate list of pythagorean triplets within min and max
	list_py_tri = [] # initialise list of list

	for a in range(max):
		for b in range(max):
			c = math.sqrt(a ** 2 + b ** 2) # c is created as a float
			if c.is_integer() and a < b and b < c:
				c = int(c)
				list_py_tri.append([a, b, c]) # append list of (a, b, c) to list of pythagorean triples
	return list_py_tri


def product(max):
	a, b, c = 0, 0, 0 # initialise values of a, b, c

	while(not sum_check(a, b, c)):
		list_py_tri = gen_py_tri(max)
		# print(list_py_tri)
		for py_tri in list_py_tri:
			# print(py_tri)
			a, b, c = py_tri[0], py_tri[1], py_tri[2]
			if sum_check(a, b, c):
			# if sum_check(list_to_no(gen_py_tri(max))):
				return a * b * c
		max += 10


if __name__ == '__main__':
	start = time()

	n = int(sys.argv[1])
	print(product(n))

	end = time()
	print (end - start, "milliseconds.")

# $ python3 9.py 300
# 31875000
# 0.8041641712188721 milliseconds.