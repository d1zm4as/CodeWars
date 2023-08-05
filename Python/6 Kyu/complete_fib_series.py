from gmpy2 import fib
def fibonacci(n):
    return [fib(x) for x in range(n)]