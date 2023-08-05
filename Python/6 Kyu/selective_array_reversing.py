def flatten(array):
    return [y for x in array for y in x]        


def sel_reverse(arr,l):
    if l == 0:return arr
    lista = [sorted(arr[i:i + l],reverse=True) for i in range(0, len(arr), l)]

    arr = flatten(lista)
    return arr
    