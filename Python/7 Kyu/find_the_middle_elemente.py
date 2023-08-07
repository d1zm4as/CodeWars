def gimme(a):
    med = len(a)//2
    b = sorted(a)[med]
    c = a.index(b)
    return c
    
