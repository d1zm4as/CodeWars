

def longest(a1, a2):
    lista1 = [x for x in a1]
    
    for y in a2:
        lista1.append(y)
    
    a = "".join(sorted(set(lista1)))
    return a

