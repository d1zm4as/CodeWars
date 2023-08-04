def prod(a):
    n = str(a)
    prod = 1
    for x in n:
        prod*=int(x)
    return prod



def persistence(n):
    a = str(n)

    cont  = 0 
    if len(a)==1:return 0
    while True:
        b = prod(a)
        if len(str(b))==1:
            break
        cont+=1
        a = b
    return cont +1