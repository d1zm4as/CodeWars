
arr,n = [1, 1, 1],2#1
arr,n = [0, 0, 0, 0, 1, 1],1#10
arr,n = [1, 4, 2, 3, 0, 5],7 #11
arr,n = [1, 3, 2, 4],4#1

def pairwise(arr, n):
    lista = []
    ref = []
    for idx,x in enumerate(arr):
        for idy,y in  enumerate(arr[:-1]):
            if  x+y ==n and idx!=idy and idx not in ref and idy not in ref:
                ref.append(idx)
                ref.append(idy)
                lista.append(idx)
                lista.append(idy)

    return sum(lista)