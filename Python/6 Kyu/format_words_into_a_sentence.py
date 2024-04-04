def format_words(arr1):
    if not arr1 or arr1==[""]:return ""
    
    arr = [x for x in arr1 if x]

    tam = len(arr)

    if tam == 1:
        return arr[0]
    if tam == 2:
        return arr[0] + " and "+ arr[1]


    ul  = arr[-1]

    su  = " and " + ul

    copy = ""

    for x in range(0,tam-1):
        if x == tam-2:
            copy+=arr[x]
        # a = arr[x]
        else:
            copy+=arr[x]
            copy+=", "
    return copy+su