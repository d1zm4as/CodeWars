arr = [4, 3, 1, 5, 6]
arr = [1, 23, 3, 4, 7]
arr = [1,2,3,4]
arr = [4, 1, 2, 3]
def twos_difference(arr): 
    lista  = []
    for x in arr:
        for y in arr:
            if y-x ==2:
                print((x,y))
                lista.append((x,y))
    return sorted(lista)