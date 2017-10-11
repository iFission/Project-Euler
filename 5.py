# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

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

def primefac(n, sieved):
	factor = []
	for i in range(len(sieved)):
		# print((sieved))
		# print("1", n, i)
		while sieved[i] and n % i == 0 and n > 1:
			# print(n, i)
			factor += [i]
			n //= i
	return factor

def LCM(n, sieved):
	LCM = []
	for i in range(len(sieved)):
		primefacd = primefac(i, sieved)
		x = 1
		for j in range(1, i + 1):
			# print(j, primefacd.count(j), LCM.count(j))
			while primefacd.count(j) > LCM.count(j):
				LCM += [j]
				# print(primefacd.count(j), LCM.count(j))
	return LCM

def product(n):
	product = 1
	sieved = sieve(n)
	LCMd = LCM(n, sieved)

	for i in range(len(LCMd)):
		product *= LCMd[i]
	return product

def product2(n): # wont return result when run with python2 when n = 43, as the product2 is bigger than max int, 9223372036854775807/219060189739591200=42.104...,
	product1 = 1
	product2 = 1
	for i in range(1, n + 1):
		while product2 % i is not 0: # when the product cant divide the new number evenly, add itself to ensure it still can divide the old numbers
			product2 += product1
			# print(i, product1, product2)
		product1 = product2
	return product2

if __name__ == '__main__':

	n = int(sys.argv[1])

	start = time()
	productd = product(n)
	print(productd)
	end = time()
	print (end - start, "milliseconds.")

	start = time()
	productd = product2(n)
	print(productd)
	end = time()
	print (end - start, "milliseconds.")