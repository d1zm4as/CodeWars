from gmpy2 import is_prime
def total(arr):
    total = 0
    for idx,x in enumerate(arr):
        if is_prime(idx):
            total+=x
    return total