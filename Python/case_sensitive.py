def case_sensitive(s):
    if not s:
        return [True,[]]
    lista = []
    
    for x in s:
        if x.isupper():
            lista.append(x)
    return [len(lista)==0,lista]