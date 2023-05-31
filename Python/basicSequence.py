def sum_of_n(n):
    cont= 0
    lista = []
    for x in range(n+1):
        if x ==0:
            lista.append(0)
        else:
            lista.append(lista[cont-1]+cont)
        cont+=1

    if n<0:
        return [x*-1 for x in lista]
    return lista








print(sum_of_n(3))