from gmpy2 import is_prime
def prime(n):
    return [x for x in range(2,n+1) if is_prime(x)]