from bisect import bisect_left
def smaller(arr):
    # Good Luck!
    right_arr = sorted(arr)
    smaller_numbers = []
    for number in arr:
        # compare number with items in right_arr
        index = bisect_left(right_arr,number)
        smaller_numbers.append(index)
        del right_arr[index]
    return smaller_numbers