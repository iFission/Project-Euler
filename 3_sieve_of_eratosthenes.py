# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# using Eratosthenes sieve

from time import time

def sieve(n):
	prime_list = [False] * 2 + [True] * (n - 1) # faster version of following
	# create a list of n Trues, later marked False
	# remaining list is all prime[index] = True
	# number = index
	# prime_list = [True for i in range(n+1)] # n + 1 so n is assign to i
	p = 2
	while (p * p < n): # reduce no. of computations, as lower multiples of p are already marked
		if prime_list[2]: #  == True
			for i in range(p * p, n + 1, p): # reduce no. of computations, as lower multiples of p are already marked
				prime_list[i] = False
		p += 1
		# print(p)
	return prime_list

if __name__ == '__main__':
	n = 10000000

	start = time()

	prime = sieve(n)
	# print([i for i in range(n) if prime[i] == True]) # list comprehension of following
	# for i in range(n):
	# 	if prime[i] == True:
	# 		print(i)

	end = time()
	print ("sieve in", end - start, "milliseconds.")