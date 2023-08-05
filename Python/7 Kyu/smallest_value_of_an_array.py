def find_smallest(n,t):
    if  t == "value":
        return min(n)
    return n.index(min(n))