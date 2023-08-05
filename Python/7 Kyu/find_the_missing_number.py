def missing_no(arr):
    mx = max(arr)
    s  = set(arr)
    for x in range(0,mx+1):
        if x not in s:
            return x
    return 100