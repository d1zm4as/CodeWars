arr = [0, 7, 0, 2, 3, 7, 0, -1, -2]

arr = [9, 7, 1, 2, 3, 7, 0, -1, -2]

def greatest_distance(arr):
    if len(arr)==len(set(arr)):return 0
    
    maior = 0
    for idx,x in enumerate(arr):
        diff = abs(arr.index(x)-idx)
        if diff>maior:
            maior=diff
    return maior
