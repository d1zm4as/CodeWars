from gmpy2 import is_prime



def check(n):
    if is_prime(n):return False
    for x in str(n):
        if x not in "2357":
            return False
    return True


def not_primes(a,b):

    return [x for x in range(a,b) if  check(x)]
