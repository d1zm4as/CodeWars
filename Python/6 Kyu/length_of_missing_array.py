def get_length_of_missing_array(arr):
    if not arr:
        return 0
    lista = []
    for x in arr:
        if not x:
            return 0
        else:
            lista.append(len(x))
    maior  = max(lista)
    menor  = min(lista)
    
    arr = sum(list(range(menor,maior+1)))
    return arr-sum(lista)