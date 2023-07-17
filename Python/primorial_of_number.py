from gmpy2 import next_prime


def num_primorial(n: int) -> int:
    p = prev = 1
    for _ in range(n):
        prev = next_prime(prev)
        p *= prev
    return p
