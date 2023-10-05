def all_non_consecutive(arr):
    lista = []
    
    atual = arr[0]
    
    for idx,x in enumerate(arr[1:]):
        if x - atual !=1 :
            lista.append({"i":idx+1, "n":x})
        atual = x
    return lista