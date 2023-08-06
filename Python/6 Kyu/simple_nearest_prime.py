from gmpy2 import is_prime
def solve(n):
    
    prox = n
    ant = n
    while True:
        if is_prime(ant):
            return ant
        if is_prime(prox):
            return prox
        prox+=1
        ant-=1
        