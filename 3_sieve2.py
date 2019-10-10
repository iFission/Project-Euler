import sys
from time import time


def sieve(n):
    prime_list = [2, 3, 5, 7, 11]

    for i in range(n):
        for prime in prime_list:
            if i % prime == 0:
                break
            else:
                prime_list.append(i)
    return prime_list


if __name__ == "__main__":
    start = time()

    print(list(sys.argv))

    n = int(sys.argv[1])
    prime = sieve(n)

    end = time()
    print("sieve in", end - start, "milliseconds.")