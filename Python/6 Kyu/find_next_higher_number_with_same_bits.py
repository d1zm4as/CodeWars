def next_higher(value):
    tam = bin(value).count("1")
    cont = value+1
    while True:
        total =  bin(cont).count("1")
        if total == tam:
            return cont
        cont+=1