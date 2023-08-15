def sum_pairs(ints, s):
    cache = set()
    for i in ints:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)
    return None