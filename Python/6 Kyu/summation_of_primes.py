from gmpy2 import is_prime
def summationOfPrimes(primes):
    return sum([x for x in range(2,primes+1) if is_prime(x)])