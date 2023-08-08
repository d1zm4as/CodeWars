def get_consective_items(items, key): 
    lista = []
    
    cont = 0
    key = str(key)
    for x in str(items):
        if x!= key:
            lista.append(cont)
            cont = 0
            
        else:
            cont+=1
    lista.append(cont)
    
    return max(lista)