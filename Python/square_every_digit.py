def square_digits(num):
    lista = [int(x) for x in str(num)]
    if sum(lista)== 0:
        return 0
    
    total = [x*x for x in lista]
    
    string =  f"{total[0]}{total[1]}{total[2]}{total[3]}"
    return int(string)
