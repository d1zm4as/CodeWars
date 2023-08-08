def solve(s):
    lista = []

    copy = []
    for idx,x in enumerate(s):
        if x == " ":
            lista.append(idx)
        else:
            copy.append(x)
    copy = copy[::-1]
    for x in lista:
        copy.insert(x," ")
    return "".join(copy)