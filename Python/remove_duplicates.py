

def distinct(seq):
    lista = ()
    for x in seq:
        if x not in lista:
            lista.add(x)
    return lista

