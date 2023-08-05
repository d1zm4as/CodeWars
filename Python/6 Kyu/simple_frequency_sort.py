from collections import Counter
def solve(arr):
    lista = sorted(arr)
    counts = Counter(lista)
    a = sorted(lista,key=counts.get,reverse=True)
    return a