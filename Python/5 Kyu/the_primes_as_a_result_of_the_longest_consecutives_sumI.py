

from gmpy2 import is_prime, next_prime

def prime_maxlength_chain(n):
    primes = []
    p = 2
    while p < n:
        primes.append(p)
        p = next_prime(p)

    max_length = 0
    result = []
    for i in range(len(primes)):
        sum_primes = 0
        for j in range(i, len(primes)):
            sum_primes += primes[j]
            if sum_primes >= n:
                break
            if is_prime(sum_primes):
                length = j - i + 1
                if length > max_length:
                    max_length = length
                    result = [sum_primes]
                elif length == max_length:
                    result.append(sum_primes)

    return sorted(result)
