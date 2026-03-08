def is_triangular(n):
    if n < 0:
        return False
    x = (8 * n + 1) ** 0.5
    return x.is_integer() and (x - 1) % 2 == 0