def solve(seq):

    lista = []

    for x in seq[::-1]:

        if x not in lista:

            lista.append(x)

    return lista[::-1]
