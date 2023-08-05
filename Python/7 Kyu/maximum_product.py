def adjacent_element_product(array):
    maior = array[0]*array[1]
    
    for x,y in zip(array,array[1:]):
        if x*y> maior:
            maior = x*y
    return maior