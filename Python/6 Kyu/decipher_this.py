def lol(x):
    lista= list(x)
    pri = ""
    cont = 0
    for y in x:
        if y.isnumeric():
            pri+=y
            cont+=1
        else:
            break
    if len(pri)==len(x):
        return chr(int(pri))
    
    item = chr(int(pri))
    novo  = item+"".join(lista[cont:])
    lista1 = list(novo)
    sec = lista1[1]
    ul = lista1[-1]
    lista1[1] = ul
    lista1[-1]=  sec
    return "".join(lista1)





def decipher_this(s):
    print(s)
    arr = s.split()
    return " ".join([lol(x) for x in arr])
