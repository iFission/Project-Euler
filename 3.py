# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def main():
	n = 600851475143
	f = 0

	for x in range(3, n):
		print("x is: {x}".format(x=x))
		if n % x == 0 and is_prime(x:
			f = x
			print(f)

	print(f)

def is_prime(n): # ensure n only has itself as a factor
	for x in range(2, n - 1): # start at 2, skip 1, stop at n-1, hence min n = 3
		print("x is: {x} for {n}".format(x=x, n=n))
		if n % x == 0:
			return False
	return True

if __name__ == '__main__':
	main()