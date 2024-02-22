def is_all_possibilities(arr):
    if not arr :
        return False
    
    return sum(list(range(len(arr)))) == sum(arr)