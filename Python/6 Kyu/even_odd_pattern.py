def even_odd(arr):
    soma = 0
    for idx,x in enumerate(arr):
        if idx%2==0:
            soma+= x
        else:
            soma*=x

    return soma