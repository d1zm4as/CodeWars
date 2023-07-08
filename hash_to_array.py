arr = {"name": "Jeremy", "age": 24, "role": "Software Engineer"}

lista = []

for x in arr:
    lol = [x,arr[x]]
    lista.append(lol)

print(sorted(lista))