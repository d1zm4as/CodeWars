def prod(arr):
    soma = 1
    for x in arr:
        soma*=x
    return soma
def max_product(arr, n):
    
    lista = sorted(arr)

    tam = len(lista)-n
    part = lista[tam:]
    return prod(part)