def descending_order(num):
    lista = sorted([x for x in  str(num)], reverse=True)
    a="".join(lista)
    return int(a)
