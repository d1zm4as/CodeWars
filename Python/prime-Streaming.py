import gmpy2
class Primes:
    @staticmethod
    def stream(n):
        
        while True:
            yield n
            n = gmpy2.next_prime(n)







