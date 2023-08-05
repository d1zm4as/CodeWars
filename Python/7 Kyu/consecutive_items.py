def consecutive(arr, a, b):
    idxa  = arr.index(a)
    idxb  = arr.index(b)
    return abs(idxa-idxb)==1
