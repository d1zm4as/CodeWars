def insert_at_indexes(frase, t, a): 
    lista = []
    for idx,x in enumerate(frase):
        print(idx,x)
        if idx in a:
            lista.append(f"{t}")
        lista.append(x)


    copy = "".join(lista)
    if max(a)>len(frase):
        copy+=t
    return copy

