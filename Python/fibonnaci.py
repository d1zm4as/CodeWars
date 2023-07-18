from gmpy2 import fib
def fibonacci(n: int) -> int:
    """Given a positive argument n, returns the nth term of the Fibonacci Sequence.
    """
    return fib(n)

print(fib(9))