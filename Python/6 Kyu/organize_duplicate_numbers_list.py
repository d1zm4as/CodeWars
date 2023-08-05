from collections import Counter
def group(arr):
    lista = []
    visto = set()
    cont = Counter(arr)
    for x in arr:
        if x not in visto:
                 
            item = [x]*cont[x]
            lista.append(item)
            visto.add(x)
            
        
    return lista