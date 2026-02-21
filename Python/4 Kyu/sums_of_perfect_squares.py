def sum_of_squares(n):
    """Return the least number of perfect square numbers which sum to n."""
    # fast checks using math.isqrt and Legendre's three-square theorem
    from math import isqrt

    # 1: n is a perfect square
    if isqrt(n) ** 2 == n:
        return 1

    # 2: n is sum of two squares? try a single sqrt loop (<= ~31623 iterations for n<=1e9)
    r = isqrt(n)
    for a in range(1, r + 1):
        b = n - a * a
        if isqrt(b) ** 2 == b:
            return 2

    # 4: Legendre's three-square theorem: numbers of form 4^k*(8m+7) need four squares
    m = n
    while m % 4 == 0:
        m //= 4
    if m % 8 == 7:
        return 4

    # Otherwise by theorem it's representable as sum of three squares
    return 3