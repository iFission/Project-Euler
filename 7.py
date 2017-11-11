# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import sys
from time import time

# implements sieve of eratosthenes, which returns a list of prime numbers below n
def sieve_of_eratosthenes(n):
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
	prime_list = sieve_of_eratosthenes(x)
	position = 0
	i = 0

	while position < y:
		i += 1
		if prime_list[i]:
			position += 1 # increse the counter if prime is detected
			# print(position)
		if i == len(prime_list) - 1:
			x *= 10 # expand the range, search again
			prime_list = sieve_of_eratosthenes(x)
	return i # return the value of the prime

if __name__ == '__main__':
	start = time()

	x = int(sys.argv[1])
	print(nth_prime(x, x))

	end = time()
	print (end - start, "milliseconds.")


# $ python3 7.py 10001
# 104743
# 0.16663813591003418 milliseconds.