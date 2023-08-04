def two_are_positive(a, b, c):
    lista = [a,b,c]
    cont = 0
    for x in lista:
        if x>0:
            cont+=1
    return cont==2