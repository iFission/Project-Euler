# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


from time import time


INT_MAX = 4000000 # define max limit

# finds the nth term of fibonacci sequence
# uses piecewise function, implemented using recursion
def get_nth_fib(n):
	# initialize with first 2 terms, 0th and 1st term as 0 and 1
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return get_nth_fib(n - 1) + get_nth_fib(n - 2)


# returns a list of even fibonacci numbers less than INT_MAX using n counter
# break out when nth exceeds INT_MAX
def get_even_list():
	n = 0
	nth_fib = get_nth_fib(n)
	even_list = []

	while nth_fib <= INT_MAX:
		if nth_fib % 2 == 0:
			even_list.append(nth_fib)
		n+=1
		nth_fib = get_nth_fib(n)
	return even_list


if __name__ == '__main__':
	start = time()

	even_list = get_even_list()
	print(even_list)
	total = sum(even_list)
	print(total)

	end = time()
	print (end - start, "milliseconds.")

# $ python3 2.py
# [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578]
# 4613732
# 10.068915843963623 milliseconds.