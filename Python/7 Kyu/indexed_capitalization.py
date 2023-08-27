def capitalize(s, ind):
    copy = ""
    lista = set(ind)
    for idx,x in enumerate(s):
        if idx in lista:
            copy+=x.upper()
        else:
            copy+=x
    return copy