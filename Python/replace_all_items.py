def replace_all(obj, find, replace):
    lista = []
    
    for x in obj:
        if x ==find:
            lista.append(replace)
        else:
            lista.append(x)
    if type(find) == int:        
        return lista
    
    return "".join(lista)