def smaller(arr):
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


    return lista