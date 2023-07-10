from gmpy2 import is_prime
def gap(g, m, n):
    ant =  n
    for x in range(m,n+1):
        if is_prime(x):
            if x-ant ==g:
                return [ant,x]
            ant = x
    return None