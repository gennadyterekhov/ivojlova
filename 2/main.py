import math
import sys
import time


# https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series
# get n'th fibonacci number recursively
def fib(n, fib_dict = {0: 0, 1: 1}):
    if n not in fib_dict:
        fib_dict[n] = fib(n - 1, fib_dict) + fib(n - 2, fib_dict)
    return fib_dict[n]


if (len(sys.argv) != 2):
    print("invalid number of arguments")
    sys.exit()


# get n from args
n = int(sys.argv[1])


# start timer
start_time = time.time()

# result is n'th fibonacci number
res = fib(n)
print(res)


# print execution time
print("\nexecution time {} seconds".format(time.time() - start_time))
