def length_of_sequence(arr,n):
    if n not in arr or len(arr)==1 or arr.count(n)!=2:return 0
    if len(arr)==2:
        return 2
    if arr[0]==n and arr[-1]==n:
        return len(arr)
    cont = 0
    seem = 1
    start = arr.index(n) + 1
    if arr[start] == n:
        return cont
    for x in arr[start:]:
        if x== n:
            return cont+2
        cont+=1