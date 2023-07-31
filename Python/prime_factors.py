def prime_factors (n):
    lista = []
    atual = 2
    while n>1:
        
        while n%atual ==0:
            n/=atual
            lista.append(atual)
        atual+=1
    return lista




print(prime_factors(12))