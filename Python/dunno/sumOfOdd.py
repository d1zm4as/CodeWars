
arr = [-3,"a",2,3]
lista = []
for x in arr:
    if type(x)!=int:
        print("FUFU")
    if x%2!=0:
        lista.append(x**3)
print(sum(lista))
