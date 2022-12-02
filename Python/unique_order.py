def unique_in_order(iterable):
    lista=[x for x in iterable]
    r = []
    if len(lista)==1:
        return lista
    if len(lista)==2:
        return [lista[0]]
    
    for x in range(0,len(lista)):
        if lista[x] == 0:
            r.append(lista[x])
            pass
        if lista[x] != lista[x-1]:
            r.append(lista[x])
    
    return r          
