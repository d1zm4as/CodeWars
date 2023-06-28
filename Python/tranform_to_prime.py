from gmpy2 import is_prime


def check(n):
    return is_prime(n)


num = [3,1,2]
num = [50,39,49,6,17,28]
soma = sum(num)

cont = 0

while not check(soma):
    soma+=1
    cont+=1

print(cont)


