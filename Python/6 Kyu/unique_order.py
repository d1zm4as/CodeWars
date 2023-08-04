def unique_in_order(iterable):
    
    if not iterable:
        return []
    r = []
    tam = len(iterable)
    if tam==1:
        return list(iterable)
    if tam==2:
        return [iterable[0]]
    r.append(iterable[0])
    for x in range(1,tam):
        if iterable[x] != iterable[x-1]:
            r.append(iterable[x])
    
    return r          
