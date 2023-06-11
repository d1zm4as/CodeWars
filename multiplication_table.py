tam = 1

lista = [x for x in range(1,tam+1)]

print(lista)
total = []
cont = 1
for x in range(tam):
    total.append([x*cont for x in lista])
    cont+=1

print(total)