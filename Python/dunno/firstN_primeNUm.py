from gmpy2 import is_prime
lista = [x for x in range(1_000_000) if is_prime(x)]
class Primes:
    def first(n):
        return lista[:n]
        