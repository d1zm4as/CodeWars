def arr(n = 0): 
    # [ the numbers 0 to N-1 ]
    n =+n
    if n == 0:
        return []
    else:
        return [x for x in range(0,int(n))]
