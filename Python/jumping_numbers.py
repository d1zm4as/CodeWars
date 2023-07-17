def jumping_number(number):
    a = str(number)
    if len(a)==1:return "Jumping!!"
    lista= [int(x) for x in a]
    
    for x,y in zip(lista,lista[1:]):
        diff = abs(x-y)
        if diff >1 or diff==0:return "Not!!"
    return "Jumping!!"