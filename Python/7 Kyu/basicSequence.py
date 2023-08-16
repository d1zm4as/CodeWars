def sum_of_n(n):
    if n==0:
        return [0]
    cont= 0
    lista = []
    for x in range(abs(n)+1):
        if x ==0:
            lista.append(0)
        else:
            lista.append(lista[cont-1]+cont)
        cont+=1

    if n<0:
        return [x*-1 for x in lista]
    return lista