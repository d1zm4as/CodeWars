arr = [0, 7, 0, 2, 3, 7, 0, -1, -2]

arr = [9, 7, 1, 2, 3, 7, 0, -1, -2]

def greatest_distance(arr):
    if len(arr)==len(set(arr)):return 0
    memo = {}
    for idx,x in enumerate(arr):
        if arr.count(x)>1:
            memo[x] = idx
    maior = 0
    for idx,x in enumerate(arr):
        if x in memo:
            a = memo[x]-idx
            if a > maior:
                maior = a
    return maior
    