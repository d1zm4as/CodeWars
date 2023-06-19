

a = [12, 10, 8, 12, 7, 6, 4, 10, 12]             # -->  12
# a = [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  #-->   3
# a = [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          #-->  12


maior = max([a.count(x) for x in set(a)])
lista = max([x for x in set(a) if a.count(x)==maior])


print(maior)
print(lista)

