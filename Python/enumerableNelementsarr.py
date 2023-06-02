def take(arr,n):
    if not arr :
        return []
    if n>len(arr):
        return arr
    return [arr[x] for x in range(0,n)]
