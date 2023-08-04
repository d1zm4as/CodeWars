from gmpy2 import is_prime
def minimum_number(num):
    soma = sum(num)

    cont = 0

    while not is_prime(soma):
        soma+=1
        cont+=1

    return cont
