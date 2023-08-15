def rotate(s):
    if not s:return []
    tam  =len(s)

    lista = []

    for x in range(1,tam):
        a = s[x:]+s[:x]
        lista.append(a)

    lista.append(s)
    return lista
    

print(rotate("hello)"))