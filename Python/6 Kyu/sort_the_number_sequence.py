def sort_sequence(sequence):
    lista = []
    sub = []
    for x in sequence:
        if x== 0:
            sub = sorted(sub)
            sub.append(x)
            lista.append(sub)
            sub = []

        else:
            sub.append(x)




    lista = sorted(lista,key = lambda x: sum(x))




    return [y for x in lista for y in x]  