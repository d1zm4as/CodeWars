

def sort_array(arr):
    b = sorted([item for item in arr if item%2 != 0])
    odd_int = 0
    for i in range(len(arr)):
        if arr[i] %2 != 0:
            arr[i] = b[odd_int]
            odd_int += 1
    return arr

