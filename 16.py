# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?


import sys
from time import time


def sum_of_power_digits(x):
	power = 2**x
	sum = 0
	for j in str(power):
		sum += int(j)
	print("2^{x} is {power}, sum is {sum}".format(x = x, power = power, sum = sum))


if __name__ == '__main__':
	start = time()

	n = int(sys.argv[1])
	sum_of_power_digits(n)

	end = time()
	print (end - start, "milliseconds.")


# $ python3 16.py 1000
# 2^1000 is 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376, sum is 1366
# 0.00017023086547851562 milliseconds.