def squared_digits_series(n):
    # Find the exponent of the largest power of 2 ≤ n
    import math
    k = int(math.log2(n))
    last_pow2 = 2 ** k

    # The generator value for position n
    if n == last_pow2:
        gen = n * 10 + 1
    else:
        gen = last_pow2 * 10 + 1

    # To get the nth term, sum all generator values up to n
    # Efficiently, for each block between powers of 2, the generator value is constant
    result = 0
    curr = 1
    while curr <= n:
        next_pow2 = curr * 2
        block_end = min(next_pow2 - 1, n)
        block_len = block_end - curr + 1
        gen_val = curr * 10 + 1 if curr == next_pow2 // 2 else (next_pow2 // 2) * 10 + 1
        result += gen_val * block_len
        curr = next_pow2
    return result