# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


from time import time
import math as m


# check whether n is a prime number by dividing itself by 2 up to n
def is_prime(n): # ensure n only has itself as a factor
	for x in range(2, n - 1): # start at 2, skip 1, stop at n-1, hence min n = 3
		# print("x is: {x} for {n}".format(x=x, n=n))
		if n % x == 0:
			return False
	return True


# returns a list of prime factors for n, by dividing n successively by increasing prime numbers
def get_prime_factors(n):
	prime_factors = []
	for x in range(3, int(m.sqrt(n))): # stop at the square root of n
		# print("x is: {x}".format(x=x))
		if n % x == 0 and is_prime(x):
			prime_factors.append(x)
			n /= x # divide n by x
	prime_factors.append(int(n))
	return prime_factors


if __name__ == '__main__':
	start = time()

	print(get_prime_factors(6008514751435))

	end = time()
	print (end - start, "milliseconds.")

# $ python3 3.py
# [5, 7, 171671850041]
# 0.22572898864746094 milliseconds.