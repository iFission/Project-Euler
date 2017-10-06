# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math as m

def main():
	n = 600851475143
	f = 1 # accounts for 1
	x = 2

	# for x in range(3, int(m.sqrt(n))): # stop at the square root of n
	while x <= int(m.sqrt(n)): # allows for update of range as n changes, <= accounts for perfect squares
		# print("x is: {x}".format(x=x))
		while n % x == 0: # doesnt have to check for prime, while checks for repeated factors
			f = x
			n = n / x
			print("factor is: {f}".format(f=f))
			if n == 1: # end when n has been fully factorised by factors <= sqrt(n), account for perfect squares
				return

		x += 1
	if n == 1:
		print("factor is {f}".format(f=f)) # accounts for 1
	else:
		print("factor is: {f}".format(f=int(n))) # as n will have at most 1 prime factor greater than sqrt(n), by doing prime fac, the last factor will be factored n, which is prime # accounts for 2

def is_prime(n): # ensure n only has itself as a factor, assumes 2 is prime
	for x in range(2, n - 1): # start at 2, skip 1, stop at n-1, hence min n = 3
		# print("x is: {x} for {n}".format(x=x, n=n))
		if n % x == 0:
			return False
	return True

if __name__ == '__main__':
	main()