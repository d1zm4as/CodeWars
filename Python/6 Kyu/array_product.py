def prod(arr,idxloc):
    total = 1
    for idx,x in enumerate(arr):
        if idx != idxloc:
            total*=x
    return total


def product_sans_n(arr):
    
    lista = []
    for idx,_ in enumerate(arr):
        lista.append(prod(arr,idx))

    return lista