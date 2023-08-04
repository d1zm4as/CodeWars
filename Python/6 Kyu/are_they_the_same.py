def comp(array1, array2):
    """
    if array1 == None or array2==None:
        return False
    
    array1.sort()
    array2.sort()
    lista2 = [(x*x) for x in array1]
    if lista2 == array2:
        return True
    return False
    """
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False
