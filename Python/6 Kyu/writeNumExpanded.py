
#a = 9
#a = 1242142421
#a = 321
#a = 12
#a=  42
a = 70304

def expanded_form(a):
    lista = [int(x) for x in str(a)][::-1]
    cont=1
    lista2 = []
    for x in lista:
        if x!=0:
            lista2.append(str(x*cont))
            cont*=10
        else:
            cont*=10
    return " + ".join(lista2[::-1])

print(expanded_form(a))