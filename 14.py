# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


import sys
from time import time


# # finds the numbef of collatz terms, using recursion
# # n keeps track the number of terms
# def collatz(i, n): # i = starting number, n = number of terms
# 	if i == 1:
# 		return n
# 	elif i % 2 == 0:
# 		print("even")
# 		n += 1
# 		i //= 2
# 		print(i, n)
# 		collatz(i, n)
# 	elif i % 2 == 1:
# 		print("odd")
# 		n += 1
# 		i = 3*i + 1
# 		print(i, n)
# 		collatz(i, n)
# 	return n


# finds the numbef of collatz terms, using iteration
# n keeps track the number of terms
def collatz(i, n): # i = starting number, n = number of terms
	while i is not 1:
		if i % 2 == 0: # use if and elif so that only one is executed in one iteration of while loop, so while loop can check for i == 1 after every if/elif
			# print("even")
			n += 1
			i //= 2
			# print(i, n)
		elif i % 2 == 1:
			# print("odd")
			n += 1
			i = 3*i + 1
			# print(i, n)
	return n


# return the number, under limit, with the longest collatz chain
def get_max_collatz(limit):
	i_max, n_max = 1, 1 # initialise

	for i in range(1, limit):
		n = collatz(i, 1) # calculate chain, with 0 as starting number of terms
		# print(i, n)
		if n > n_max: # update max i and n
			i_max = i
			n_max = n

	return i_max, n_max


if __name__ == '__main__':
	start = time()

	n = int(sys.argv[1])
	print(get_max_collatz(n))

	end = time()
	print (end - start, "milliseconds.")


# $ python3 14.py 1000000
# (837799, 525)
# 20.788210153579712 milliseconds.