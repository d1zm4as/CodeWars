def arr_check(arr):
    for x in arr:
        if type(x)!=list:
            return False
    return True