def multiplication_table(tam):
    lista = [x for x in range(1,tam+1)]

    total = []
    cont = 1
    for x in range(tam):
        total.append([x*cont for x in lista])
        cont+=1

    return total