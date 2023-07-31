def first_non_consecutive(arr):
    for x in range(1,len(arr)):
        if arr[x]-arr[x-1]>1:
            return arr[x]
    return False