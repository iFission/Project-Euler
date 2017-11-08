import sys
from time import time


if __name__ == '__main__':
	start = time()

	n = int(sys.argv[1])

	end = time()
	print (end - start, "milliseconds.")