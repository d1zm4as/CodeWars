def data_reverse(data1):
    lista = []
    size = 8
    arr = [data1[i:i + size] for i in range(0, len(data1), size)]
    
    for x in arr[::-1]:
        for y in x:
            lista.append(y)
    return lista           