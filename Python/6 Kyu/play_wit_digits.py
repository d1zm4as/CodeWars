def dig_pow(n, p):
    lista = [int(x) for x in  str(n)]
    total = []
    cond = p
    for x in lista:
        a  = x**cond
        total.append(a)
        cond+=1
    div = sum(total)//n
    if div*n == sum(total):
        return div
    else:
        return -1
