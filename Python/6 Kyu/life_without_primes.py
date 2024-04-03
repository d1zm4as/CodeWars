from gmpy2 import is_prime

def check(n):
    a  =str(n)
    lista = {"1","4","6","8","9","0"}
    for x in a:
        if x not in lista:
            return False
    return True

def solve(n):
    cont = 0
    lista = []
    x = 1
    while cont < n+1:
        if not is_prime(x) and check(x):
            lista.append(x)
            cont+=1
        x+=1
    return lista[-1]
    