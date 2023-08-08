def powers_of_two(n):
    """
    lista = []
    for x in range(0,n+1):
        lista.append(2**x)
    return lista
    """
    return [(2**x) for x in range(0,n+1)]
