def prod(arr):
    soma = 1
    for x in arr:
        soma*=x
    return soma

lista = [10, 8, 3, 2, 1, 4, 10]


n = 5


lista = sorted(lista)

tam = len(lista)-n
part = lista[tam:]

print(lista)
print(prod(part))