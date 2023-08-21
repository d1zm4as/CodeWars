def find_array(a,b):
    if not a or not b:
        return []
    
    arr = []
    for idx,_ in enumerate(a):
        arr.append(idx)
    
    lista = []
    
    for x in b:
        if x in arr:
            lista.append(a[x])
    return lista
