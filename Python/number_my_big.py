def narcissistic( value ):
    toString = str(value)

    lista = [int(x) for x in toString]


    

    total = []
    
    for y in lista:
        a = y**len(lista)
        total.append(a)


    if sum(total)==value:
        return True
    else:
        return False
    

    
print(narcissistic(7))
