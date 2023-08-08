def row_weights(lista):
    
    soma1 = 0

    soma2 = 0

    for idx,x in enumerate(lista):
        if idx%2==0:
            soma1+=x
        else:
            soma2+=x

    return (soma1,soma2)