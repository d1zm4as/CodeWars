def sum_consecutives(s): 
    
    lista = []

    atual = s[0]
    copy = atual
    for x in s[1:]:
        if x== atual:
            copy+=atual
            atual = x
        else:
            lista.append(copy)
            copy = 0 
            atual = x
            copy = x
    lista.append(copy)
    return lista


print(sum_consecutives([1,4,4,4,0,4,3,3,1]))