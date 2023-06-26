from gmpy2 import is_prime

def all_prime_digits(n):
    for d in str(n):
        if d not in "2357":
            return False
    return True
prime_array = [x for x in range(10, 10**7+1) if is_prime(x) and all_prime_digits(x)]
def get_total_primes(a, b):
    
    return len([p for p in prime_array if a <= p < b])