def two_sum(num, t):
    lista = {}
    for idx,x in enumerate(num):
        diff = t-x
        if diff in lista: 
            return [lista[diff],idx]
        lista[x] = idx
