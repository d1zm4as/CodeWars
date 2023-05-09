def sum_array(arr):
    return 0 if not arr or len(arr)==1 else sum(arr)-min(arr)-max(arr)
