def array_conversion(arr):
    iteration = 1
    while len(arr) > 1:
        if iteration % 2 == 1:
            arr = [arr[i] + arr[i + 1] for i in range(0, len(arr) - 1, 2)]
        else:
            arr = [arr[i] * arr[i + 1] for i in range(0, len(arr) - 1, 2)]
        iteration += 1
    return arr[0]