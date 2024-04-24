def swap(s):
    lista = ("a","e","i","o","u","A","E","I","O","U")
    copy = ""    
    for x in s :
        if x in lista:
            copy+=x.upper()
        else:
            copy+=x
    return copy
