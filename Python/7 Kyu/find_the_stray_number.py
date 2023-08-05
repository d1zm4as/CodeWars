def stray(arr):
    lista = sorted(arr)
    return lista[0] if lista.count(lista[0])==1 else lista[-1] 
