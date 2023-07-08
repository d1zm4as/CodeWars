s = "Hello"

tam  =len(s)

lista = []

for x in range(1,5):
    a = s[x:]+s[:x]
    lista.append(a)

print(lista)
lista.append(s)
print(lista)