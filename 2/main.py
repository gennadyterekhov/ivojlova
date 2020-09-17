import math
import sys

# get n'th fibonacci number recursively
def fib(n):
    if (n < 2):
        return n
    return fib(n - 1) + fib(n - 2)


if (len(sys.argv) != 2):
    print("invalid number of arguments")
    sys.exit()


# get n from args
n = int(sys.argv[1])

# result is n'th fibonacci number
res = fib(n)
print(res)


