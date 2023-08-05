from gmpy2 import fib
def all_fibonacci_numbers():
    a, b = 0, 1
    for i in range(1, 100000):
        a, b = b, a + b
        yield a        
