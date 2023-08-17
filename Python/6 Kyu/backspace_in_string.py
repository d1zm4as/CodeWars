def clean_string(s):
    lista = []
    for idx,x in enumerate(s):
        if x == "#" :
            if len(lista)==0:
                continue
            lista.pop()
        else:
            lista.append(x)
    if len(lista)==0:
        return ""
    return "".join(lista)