s = "hello case"

lista = []

for x in s.split():
    lista.append(x.title())

print(lista)

print("".join([x.title() for x in s.split()]))
