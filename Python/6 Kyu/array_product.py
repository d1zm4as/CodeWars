def prod(a):
    total = 1
    for x in a:
        total*=x
    return total

a = [1,2,3,4]

ref = prod(a)

lista = []

for x in a:
    lista.append(int(ref/x))
print(lista)