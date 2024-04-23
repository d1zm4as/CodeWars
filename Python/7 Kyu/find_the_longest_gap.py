def gap(n):
    b = bin(n)[2:]

    cont = 0
    maior = 0
    for x in b:
        if x=="0":
            cont+=1
        else:
            maior = max(maior,cont)
            cont = 0
    return maior