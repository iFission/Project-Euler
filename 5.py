# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


import sys
from time import time


# finds the prime factors of all numbers from 1 to 20
# calculate the LCM from the prime factors


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


# returns a list of prime factors for n, by dividing n successively by increasing prime numbers
# checks for prime number using prime_list from sieve_of_eratosthenes
def get_prime_factors(n, prime_list):
	prime_factors = []
	for i in range(n + 1): # loops through 0 to n, accounts for the case when n is a prime number
		# print((prime_list))
		# print("1", n, i)
		while prime_list[i] and n % i == 0 and n > 1:
			# print(n, i)
			prime_factors += [i]
			n //= i
	return prime_factors


# finds the lowest common multiple by filtering through list of prime numbers and n
# n will take the range of (2, n + 1), > 2, 3, ..., n
def get_LCM(n, prime_list):
	LCM = []
	for i in range(2, n + 1):
		prime_factors = get_prime_factors(i, prime_list)
		x = 1
		for j in range(1, i + 1):
			# print(j, prime_factors.count(j), LCM.count(j))
			while prime_factors.count(j) > LCM.count(j): # keep adding prime factor j until LCM has the same number as i
				LCM += [j]
				# print(prime_factors.count(j), LCM.count(j))
	return LCM


def get_product(n):
	product = 1
	prime_list = sieve_of_eratosthenes(n)
	LCM = get_LCM(n, prime_list)

	for i in range(len(LCM)):
		product *= LCM[i]
	return product


# find the product by iterating through 1 to n + 1, making sure the product2 is divisible by i, by adding the previous product1 until product2 is a multiple
def get_product_2(n): # wont return result when run with python2 when n = 43, as the product2 is bigger than max int, 9223372036854775807/219060189739591200=42.104...,
	product1 = 1 # placeholder for the first product
	product2 = 1 # placeholder for the second product
	for i in range(1, n + 1):
		while product2 % i is not 0: # when the product cant divide the new number evenly, add itself to ensure it still can divide the old numbers
			product2 += product1
			# print(i, product1, product2)
		product1 = product2
	return product2


if __name__ == '__main__':
	start = time()

	n = int(sys.argv[1])
	product = get_product(n)
	print(product)

	end = time()
	print (end - start, "milliseconds.")


	start = time()

	product = get_product_2(n)
	print(product)

	end = time()
	print (end - start, "milliseconds.")

# $ python3 5.py  20
# 232792560
# 0.00016164779663085938 milliseconds.
# 232792560
# 1.1920928955078125e-05 milliseconds.