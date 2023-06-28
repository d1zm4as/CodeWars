from gmpy2 import is_prime

start = 7000

stop = 7100

def pali(x):
    return str(x)==str(x)[::-1]




lista = [x for x in range(start,stop+1) if is_prime(x) and not pali(x)]


arr = []
# int(str(x)[::-1])
for x in lista:
    lol = int(str(x)[::-1])
    if is_prime(lol):
        arr.append(x)
    

print(arr)

print(lista)