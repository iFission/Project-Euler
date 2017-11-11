# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?


import sys
from time import time
from functools import reduce


def get_product(list_number): # calculates the product of a list_number of numbers
	# return reduce(lambda x, y : x * y, list_number)
	product = 1
	# print(list_number)
	for i in list_number:
		i = i[0]
		# print(i)
		product *= i
		# print(product)
	return product


# only need 4 directions, as the other directions will generate the same list_number of numbers from the other side
def product_u(matrix, x, y, n): # calculates the product of up direction
	list_number = []
	for i in range(n):
		if x - i >= 0 : # check cell exists by ensuring x is at least 0
		# if matrix[x - i][y]: # check cell exists
			list_number.append([matrix[x - i][y]])
			# print("appended" + str([matrix[x - i][y]]))
		else: # when one of the cells don't exist, return None
			return None
	return list_number, get_product(list_number) # returns the product of the list_number if there are no cells that don't exist


def product_ur(matrix, x, y, n): # calculates the product of up-right direction
	list_number = []
	for i in range(n):
		if x - i >= 0 and y + i < 20: # check cell exists, ensuring y is less than 20 (at most 19)
			list_number.append([matrix[x - i][y + i]])
		else: # when one of the cells don't exist, return None
			return None
	return list_number, get_product(list_number) # returns the product of the list_number if there are no cells that don't exist


def product_r(matrix, x, y, n): # calculates the product of right direction
	list_number = []
	for i in range(n):
		if y + i < 20 and y + i < 20: # check cell exists
			list_number.append([matrix[x][y + i]])
		else: # when one of the cells don't exist, return None
			return None
	return list_number, get_product(list_number) # returns the product of the list_number if there are no cells that don't exist


def product_rd(matrix, x, y, n): # calculates the product of right down direction
	list_number = []
	for i in range(n):
		if x + i < 20 and y + i < 20: # check cell exists
			list_number.append([matrix[x + i][y + i]])
		else: # when one of the cells don't exist, return None
			return None
	return list_number, get_product(list_number) # returns the list_number and the product of the list_number if there are no cells that don't exist


def product_directions(matrix, x, y, n, directions):
	list_number_max = []
	product_max = 0
	direction_max = ""
	list_number = []
	product = 0

	for direction in directions:
		if direction is "u":
			if product_u(matrix, x, y, n) is not None:
				list_number, product = product_u(matrix, x, y, n)
		if direction is "ur":
			if product_ur(matrix, x, y, n) is not None:
				list_number, product = product_ur(matrix, x, y, n)
		if direction is "r":
			if product_r(matrix, x, y, n) is not None:
				list_number, product = product_r(matrix, x, y, n)
		if direction is "rd":
			if product_rd(matrix, x, y, n) is not None:
				list_number, product = product_rd(matrix, x, y, n)
		if product > product_max:
			list_number_max, product_max = list_number, product
	return list_number_max, product_max, direction_max


def product_coordinate(n):
	matrix = [
				[8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8],
				[49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0],
				[81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65],
				[52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91],
				[22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
				[24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50],
				[32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
				[67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21],
				[24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
				[21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95],
				[78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92],
				[16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57],
				[86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58],
				[19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40],
				[4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66],
				[88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69],
				[4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36],
				[20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16],
				[20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54],
				[1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]
			]
	directions = ["u", "ur", "r", "rd"]
	x_max, y_max = 0, 0
	list_number_max = []
	product_max = 0
	direction_max = ""

	for x in range(len(matrix)): # len(matrix) returns the number of rows
		for y in range(len(matrix[0])): # len(matrix[0]) returns the number of columns
			list_number, product, direction = product_directions(matrix, x, y, n, directions)
			if product > product_max:
				x_max, y_max, list_number_max, product_max, direction_max = x, y, list_number, product, direction
				# print("Max product occurs at ", x_max, y_max)
				# print("The direction is " + direction_max)
				# print("The numbers are ", list_number_max)
				# print("The product is ", product_max)

	print("Max product occurs at ", x_max, y_max)
	print("The direction is " + direction_max)
	print("The numbers are ", list_number_max)
	print("The product is ", product_max)


if __name__ == '__main__':
	start = time()

	n = int(sys.argv[1])
	product_coordinate(n)

	end = time()
	print (end - start, "milliseconds.")


# $ python3 11.py 4
# Max product occurs at  15 3
# The direction is
# The numbers are  [[87], [97], [94], [89]]
# The product is  70600674
# 0.005494117736816406 milliseconds.