def nb_dig(n, d):
    a = "".join([str(x*x) for x in range(0,n+1)])
    return a.count(str(d))
