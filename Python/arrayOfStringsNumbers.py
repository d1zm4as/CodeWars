def to_float_array(arr): 
    lista = []
    for x in arr:
        if "." in x:
            lista.append(float(x))
        else:
            lista.append(int(x))
    
    return lista