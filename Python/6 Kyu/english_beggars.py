def beggars(values, n):
    if n<=0:
        return []

    if n==1:
        return sum(values)
    
    lista = []
    for i in range(n):
        lista.append(sum(values[i::n]))
    return lista