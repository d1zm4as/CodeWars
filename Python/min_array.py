def min_sum(arr):
    arr = sorted(lista)

    tam = len(arr)
    half= tam//2
    a = arr[:half]
    b = arr[half:tam][::-1]
    return sum([(x*y) for x,y in zip (arr[:half],arr[half:tam][::-1])])