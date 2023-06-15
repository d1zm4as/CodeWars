lista = [1,3,1]
lista = [4,7,5,7]
lista = [4,8,1,4]

a = "".join(sorted([str(x) for x in set(lista)]))

print(a)
print(int(a))

