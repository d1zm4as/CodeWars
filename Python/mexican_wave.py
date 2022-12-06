def wave(b):
    tam = len(b)
    idx = 0
    lista = []
    while idx<tam:
        c = ""
        for x in range(tam):
            
            if b[idx]==" ":
                continue
            if idx == x:
                c+=b[idx].upper()
            else:
                c+=b[x]
        idx+=1
        lista.append(c)
    return [x for x in lista if x != ""]
  
  
