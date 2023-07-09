def miss_nums_finder(arr):
    mx = max(arr)
    s  = set(arr)
    return [x for x in range(1,mx) if x not in s]
    