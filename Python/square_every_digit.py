def square_digits(num):
    lista = [int(x) for x in str(num)]
    if sum(lista)== 0:
        return 0
    
    total = [str(x*x) for x in lista]
    
    return int("".join(total))