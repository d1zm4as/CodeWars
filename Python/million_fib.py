import gmpy2

def fib(n):
    return gmpy2.fib(abs(n)) * (-1 if n < 0 and n % 2 == 0 else 1)