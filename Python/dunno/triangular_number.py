def tri(n):
    return sum(list(range(1,n+1)))




n = 4

lista = sum([tri(x) for x in range(n+1)])


print(lista)
