from gmpy2 import is_prime

def twin_prime(n):
    return sum(is_prime(i) and is_prime(i + 2) for i in range(n))
    