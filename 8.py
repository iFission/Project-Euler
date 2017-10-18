# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450

# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

import sys
from time import time

def product_func(number, n, index): # calculates the product of n adjacent digits, start at number[index], end at number[index+n-1]
	product = 1

	for i in range(index, index + n): # steps over n numbers
		product *= int(number[i]) # compute the product, convert number[index] from str to int
		# print(number[i], product)
	return product, index # returns product and index

def largest_func(number, n):# finds the largest product of n adjacent numbers, from number
	product_largest = 0
	index_largest = 0
	for i in range(len(number) - n + 1):
	# range restricted to stop at 1000-n+1 th number,
	# eg: 10 digit number 1 2 3 4 5 6 7 8 9 10
	# 4 adjacent digits
	# need to stop at 7, to allow for 7 8 9 10 to be computed
		product, index = product_func(number, n, i)
		if product > product_largest:
			product_largest, index_largest = product, index
	return product_largest, index_largest

if __name__ == '__main__':

	number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
	number = str(number) # convert number to str to allow for [] access
	n = int(sys.argv[1]) # number of adjacent digits

	start = time()

	# print(product_func(number, n, 17))
	product_largest, index_largest = largest_func(number, n)
	print(product_largest, index_largest, [number[i] for i in range(index_largest, index_largest + n)])

	end = time()
	print (end - start, "milliseconds.")