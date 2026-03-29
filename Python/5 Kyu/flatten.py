def flatten(*args):
    lista = []
    for x in args:
        if type(x)==list:
            lista.extend(flatten(*x))
        else: lista.append(x)
    return lista    