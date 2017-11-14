# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?


import sys
from time import time
import math as m



# calculate nth triangle number
# find its prime factors
# use the powers of the prime factors to find the number of divisors
# input number of divisors, limit to calculate prime list

# find nth triangle number using sum of ap
# follows arithmetic progression with u1 = 1, d = 2
def get_nth_tri_no(n):
	return (n + n**2)//2


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
	for i in range(2, int(m.sqrt(n))): # loops through 0 to n, accounts for the case when n is a prime number
		# print((prime_list))
		# print("1", n, i)
		# print(i)
		# print(len(prime_list))
		while prime_list[i] and n % i == 0 and n > 1:
			# print(n, i)
			prime_factors += [i]
			n //= i
	print(prime_factors)
	return prime_factors


# find the number of divisors a number n has, using the formula:
# n = A^a * B^b * C^c
# divisors = (a+1)(b+1)(c+1)
def get_divisors(n, prime_list):
	prime_factors = get_prime_factors(n, prime_list)
	divisors = 1 # initialise divisors for multiplication later
	for i in range(n):
		if prime_factors.count(i): # find prime factor A exist
			divisors *= (prime_factors.count(i) + 1) # multiply by a+1
	print(divisors)
	return divisors


# input start, n (number of divisors required), limit
def get_nth_tri_no_500_div(n, limit):
	i = 1 # initialise i as start
	tri_no = get_nth_tri_no(i)
	prime_list = sieve_of_eratosthenes(limit)
	divisors = get_divisors(tri_no, prime_list)

	while divisors <= n: # keep increasing i (go to the next triangle number) until the number of divisors exceeds 500
		i += 1
		tri_no = get_nth_tri_no(i)

		# increase the limit by 2 times, for the range of prime list, if the triangle number exceeds the limit
		if tri_no >= limit:
			limit *= 2
			prime_list = sieve_of_eratosthenes(limit)
			print("limit increased" + str(limit))

		print("triangle number is " + str(tri_no), "limit is " + str(limit))
		divisors = get_divisors(tri_no, prime_list)

	# print("triangle number is " + str(get_nth_tri_no(i)))
	return get_nth_tri_no(i)


if __name__ == '__main__':
	start = time()

	n, limit = int(sys.argv[1]), int(sys.argv[2])
	print(get_nth_tri_no_500_div(n, limit))

	end = time()
	print (end - start, "milliseconds.")


# $ python3 12.py 500 10000
# triangle number is 76564125 limit is 81920000
# [3, 3, 5, 5, 5, 11, 23, 269]
# 96
# triangle number is 76576500 limit is 81920000
# [2, 2, 3, 3, 5, 5, 5, 7, 11, 13, 17]

# with sqrt range
# triangle number is 76576500 limit is 81920000
# [2, 2, 3, 3, 5, 5, 5, 7, 11, 13, 17]
# 576
# 76576500
# 51410.40483188629 milliseconds.
# 576
# 76576500
# 69472.91197299957 milliseconds.