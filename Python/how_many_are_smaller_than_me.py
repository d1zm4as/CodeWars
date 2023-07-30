arr = [5, 4, 3, 2, 1]
arr =  [1, 2, 0]
lista=  []


cont = 0

while cont<len(arr):
    ref = arr[cont]
    total =  0
    for x in arr[cont+1:]:
        if x<ref:
            total+=1
    lista.append(total)
    cont+=1


print(lista)
