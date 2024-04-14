def sort_string(a, b):
    lista = []
    extra = ""
    for x in a:
        if x in b:
            lista.append(x)
        else:
            extra+=x
    if len(lista)>0:
        lista = sorted([x for x in lista],key = lambda x: b.index(x))
        return "".join(lista)+extra
    else:
        return a
