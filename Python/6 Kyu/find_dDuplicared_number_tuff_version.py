from collections import Counter

def find_dup(arr):
    cont = Counter(arr)
    for x in arr:
        if cont[x]>1:
            return x