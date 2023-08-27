def squares(x, n):
    if n <=0:return []
    atual = x
    lista = [atual]
    cont = 1
    while cont<n:
        atual *=atual
        lista.append(atual)
        cont+=1
    return lista


