def merge_arrays(arr1, arr2):
    for x in arr1:
        if x in arr2:
            pass
        else:
            arr2.append(x)
    return sorted([x for x in set(arr2)])
