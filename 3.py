# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# using Eratosthenes sieve

def main():
	n = 600851475143
	prime = sieve(n)

	print([i for i in range(n) if prime[i] == True]) # list comprehension of following
	# for i in range(n):
	# 	if prime[i] == True:
	# 		print(i)

def sieve(n):
	prime_list = [True for i in range(n+1)]
	p = 2
	while (p * p < n):
		if prime_list[2] == True:
			for i in range(p * 2, n + 1, p):
				prime_list[i] = False
		p = p + 1
		# print(p)
	return prime_list

if __name__ == '__main__':
	main()