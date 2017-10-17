# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import sys
from time import time

def sieve(n):
	prime_list = [False] * 2 + [True] * (n - 1) # faster version of following, + to add arrays together
	# create a list of n Trues, later marked False
	# remaining list is all prime[index] = True
	# number = index
	# prime_list = [True for i in range(n+1)] # n + 1 so n is assign to i
	p = 2
	while (p * p < n): # reduce no. of computations, as lower multiples of p are already marked
		if prime_list[p]: #  == True
			for i in range(p * p, n + 1, p): # reduce no. of computations, as lower multiples of p are already marked, increase by multiple p
				prime_list[i] = False
		p += 1
		# print(p)
	return prime_list

def nth_prime(x, y): # first n defines the range to search through, second n defines the desired nth position of prime

	prime = sieve(x)

	position = 0
	for i in range(len(prime)):
		if prime[i]:
			position += 1 # increse the counter if prime is detected
			# print(position)
		if position == y: # when the counter matches desired position
			# if i is None:
			print(i)
			return i # return the value of the prime
		if i == len(prime) - 1:
			x *= 10 # expand the range, search again
			nth_prime(x, y)

if __name__ == '__main__':

	x = int(sys.argv[1])

	start = time()

	nth_prime(x, x)

	end = time()
	print (end - start, "milliseconds.")