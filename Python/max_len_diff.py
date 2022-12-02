def mxdiflg(a1, a2):
    diff = 0
    
    for x in a1:
        for y in a2:
            a = abs(len(x)-len(y))
            if a>diff:
                diff = a
    if len(a1)==0 or len(a2)==0:
        return -1
    return diff
    
