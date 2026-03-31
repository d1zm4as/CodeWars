from gmpy2 import mpz, next_prime


def primes():
    """Infinite prime generator optimized via gmpy2.next_prime."""
    n = mpz(1)
    _next = next_prime
    while True:
        n = _next(n)
        yield n


class Primes:
    @staticmethod
    def stream():
        return primes()

