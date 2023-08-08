from gmpy2 import is_prime
def odd_not_prime(n):
    return len([x for x in range(n+1) if not is_prime(x) and x%2!=0])