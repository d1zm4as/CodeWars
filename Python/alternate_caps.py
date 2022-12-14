def capitalize(s):
    a = "".join([ x.upper() if idx %2==0 else x for idx,x in enumerate(s)])
    return [a,a.swapcase()]
