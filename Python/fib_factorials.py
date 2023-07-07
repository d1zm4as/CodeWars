from gmpy2 import fac,fib


lista = [fib(x) for x in range(4)]

print(sum([fac(x) for x in lista]))
from gmpy2 import fac,fib
def sum_fib(n):
    lista = [fib(x) for x in range(n)]
    return sum([fac(x) for x in lista])