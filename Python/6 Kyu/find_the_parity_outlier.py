from gmpy2 import is_even

def find_outlier(integers):
    """Given an array of integers, return the one that differs from the others.

    The array will have a length of at least 3, and all integers will be
    either even or odd except for a single integer N. Return this "outlier"
    N.
    """
    even_count = 0
    odd_count = 0
    last_even = None
    last_odd = None

    for num in integers:
        if is_even(num):
            even_count += 1
            last_even = num
        else:
            odd_count += 1
            last_odd = num

        # We can stop early if we already have enough evidence to determine the outlier
        if even_count > 1 and odd_count > 0:
            return last_odd
        if odd_count > 1 and even_count > 0:
            return last_even

    # If we finish the loop without returning, it means the outlier is the one that has only one count
    return last_even if even_count == 1 else last_odd