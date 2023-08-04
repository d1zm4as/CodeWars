def solution(s):
    """
    lista= [x for x in s]

    for x in lista:
        if x.isupper()==True:
            a = lista.index(x)
            lista[a]=f" {x}"
    return "".join(lista)
    """
    return ''.join(' ' + x if x.isupper() else x for x in s)
