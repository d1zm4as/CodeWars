def remember(s):
    lista = []
    
    seen = []
    
    for x in s:
        if x in seen:
            if x not in lista:
                lista.append(x)
        else:
            seen.append(x)
    return lista