def contain_all_rots(a, arr):
    lista = []
    cont = 0
    for x in range(len(a)):
        rot = a[x:]+a[:x]
        lista.append(rot)
    
    if a == "":
        return True
    
    for x in lista:
        if x in arr:
            cont+=1
    if cont== len(lista):
        return True
    return False
