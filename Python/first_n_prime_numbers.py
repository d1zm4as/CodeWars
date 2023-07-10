from gmpy2 import is_prime
class Primes:
    def first(n):
        lista = []
        cont = 0
        while len(lista)<n:
            if is_prime(cont):
                lista.append(cont)
            cont+=1
        return lista