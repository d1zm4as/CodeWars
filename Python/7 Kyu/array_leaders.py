def array_leaders(lista):
    arr = []

    cont = 0

    for x in lista:
        if x*2 >sum(lista[cont:]):
            arr.append(x)
        cont+=1 
    return arr
    