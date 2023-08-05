def distinct(seq):
    lista = []
    for x in seq:
        if x not in lista:
            lista.append(x)
    return lista

