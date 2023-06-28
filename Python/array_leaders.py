lista = [1,2,3,4,0]
lista = [-1,-29,-26,-2]
lista = [5,2]
arr = []

cont = 0

for x in lista:
    print(x,lista[cont:])
    if x*2 >sum(lista[cont:]):
       arr.append(x)
    cont+=1 
print(arr)
