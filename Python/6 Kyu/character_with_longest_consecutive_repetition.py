def longest_repetition(s): 
    if not s:
        return ("",0)
    lista = []

    atual = s[0]
    copy = atual
    for x in s[1:]:
        if x== atual:
            copy+=atual
            atual = x
        else:
            lista.append(copy)
            copy = ""
            atual = x
            copy = x
    lista.append(copy)
    a = max(lista,key  = len)
    return (a[0],len(a))