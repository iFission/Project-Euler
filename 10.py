# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

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

def sum_primes(n):
	prime_list = sieve(n)
	sum = 0

	for i in range(len(prime_list)):
		if prime_list[i]:
			# print(i)
			sum += i
	return sum

if __name__ == '__main__':

	n = int(sys.argv[1])

	start = time()

	print(sum_primes(n))

	end = time()
	print (end - start, "milliseconds.")

# $ python3 10.py 2000000
# 142913828922
# 0.35898399353027344 milliseconds.