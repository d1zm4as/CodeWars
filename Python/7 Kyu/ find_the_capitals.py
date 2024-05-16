def capital(capitals): 
    lista = []
    for x in capitals:
        ref = list(x.keys())
        f = ref[0]
        las = ref[1]
        s  = f"The capital of {x[f]} is {x[las]}"
        lista.append(s)
    return lista
    