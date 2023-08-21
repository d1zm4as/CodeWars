def sum_arrays(a,b):
    if not b:
        return a
    if not b and not a:
        return []
    if not a:
        if b[0] == 0:
            return b[1:]
        return b
    copyA = ""
    for x in a:
        copyA+=str(x)

    copyB = ""
    for x in b:
        copyB+=str(x)


    soma = int(copyA)+int(copyB)



    lista= []

    turn = str(soma)
    if soma<0:
        lista.append(int(turn[1])*-1)
        for x in turn[2:]:
            lista.append(int(x))

    else:
        lista.append(int(turn[0]))
        for x in turn[1:]:
                lista.append(int(x))
    return lista