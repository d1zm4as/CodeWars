

# https://en.wikipedia.org/wiki/Prime-counting_function

from math import isqrt
from functools import cache
from bisect import bisect
import sys

sys.setrecursionlimit(10**5)

# https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
def rwh_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

PRIMES = rwh_primes(10**7)

@cache
def phi(m, n):
    if n == 1 or m < 1: return (m + 1) // 2
    p = PRIMES[n - 1]
    # https://ideone.com/SnhEQA
    if p * p >= m and m < PRIMES[-1]:
        return bisect(PRIMES, m) - n + 1
    return phi(m, n - 1) - phi(m // p, n - 1)

def pi(m):
    if m <= PRIMES[-1]:
        return bisect(PRIMES, m)
    n = pi(int((m + 0.5) ** (1 / 3)))
    mu = pi(isqrt(m)) - n
    return phi(m, n) + n * (mu + 1) + mu * (mu - 1) // 2 - 1 - sum(pi(m // PRIMES[n + k]) for k in range(mu))

count_primes_less_than = pi

