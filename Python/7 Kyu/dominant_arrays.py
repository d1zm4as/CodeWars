def solve(arr):

    lista = []

    tam = len(arr)

    cont = 0

    while cont < tam:
        atual  = arr[cont]
        ref = max(arr[cont:])
        if atual>=ref and atual not in lista:
            lista.append(atual)
        cont+=1
    return lista