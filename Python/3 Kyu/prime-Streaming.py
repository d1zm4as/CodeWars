import gmpy2
class Primes:
    @staticmethod
    def stream():
        n = 2
        while n<100000000000:
            yield n
            n = gmpy2.next_prime(n)


