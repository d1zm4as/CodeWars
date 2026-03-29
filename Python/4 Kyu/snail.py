def snail(array):
    res = []
    while array and array[0]:
        res += array.pop(0)
        array = list(zip(*array))[::-1]
    return res
