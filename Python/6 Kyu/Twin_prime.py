from gmpy2 import is_prime
def is_twinprime(n):
    if not is_prime(n):
        return False
    ant = n-2
    prox = n+2
    return is_prime(ant)or is_prime(prox)