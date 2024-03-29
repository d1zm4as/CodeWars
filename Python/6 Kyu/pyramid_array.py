def pyramid(n):
    if n == 0 : return []
    lista = []

    for x in range(1,n+1):
        lista.append([1]*x)
    return lista