def delete_digit(n):
    s = str(n)

    lista = []

    for idx,x in enumerate(s):
        lista.append(int("".join([v for i, v in enumerate(s) if i != idx])))

    return max(lista)
