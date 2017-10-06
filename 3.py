# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math as m

def main():
	n = 6008514751435
	f = 0
	x = 2

	# for x in range(3, int(m.sqrt(n))): # stop at the square root of n
	while x < int(m.sqrt(n)): # allows for update of range as n changes
		# print("x is: {x}".format(x=x))
		if n % x == 0 and is_prime(x) and f < x:
			f = x
			n = int(n / x)
			# if is_prime(int(n / x)) and f < x: # check the complementary factor is prime
			# 	f = x
			print(f)
		x += 1
	if n == 1:
		print(f) # as n will have at most 1 prime factor greater than sqrt(n), by doing prime fac, the last factor will be factored n, which is prime
	else:
		print(n) # accounts for 1 and 2

def is_prime(n): # ensure n only has itself as a factor, assumes 2 is prime
	for x in range(2, n - 1): # start at 2, skip 1, stop at n-1, hence min n = 3
		# print("x is: {x} for {n}".format(x=x, n=n))
		if n % x == 0:
			return False
	return True

if __name__ == '__main__':
	main()