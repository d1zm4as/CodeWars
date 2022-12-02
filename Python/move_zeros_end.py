

def move_zeros(lst):
    lista = [x for x in lst if x==0]
    lista1 = [y for y in lst if y!=0]
    for z in lista:
        lista1.append(z)
    return lista1

