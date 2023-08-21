def partlist(a):
    lista = []
    cont = 1
    for x in range(len(a)-1):
        atuais = " ".join(a[:cont])
        resto = " ".join(a[cont:])

        lista.append(tuple([atuais,resto]))

        cont+=1
    return lista
    