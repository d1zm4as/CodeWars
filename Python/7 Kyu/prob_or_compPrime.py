from gmpy2 import is_prime

def prime_or_composite(n):
    return "Probable Prime" if is_prime(n) else "Composite"