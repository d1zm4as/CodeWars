def capitals(a):
    idx = 0
    lista = []
    for x in a:
        if x.isupper():
            lista.append(idx)
        idx+=1
    return lista
