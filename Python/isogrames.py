ef is_isogram(string):
    lista1 = set(x.lower() for x in string)
    lista2 = [y for y in string]
    
    if len(lista1)==len(lista2):
        return True
    else:
        return False
