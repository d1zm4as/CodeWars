
def sort_by_value_and_index(arr):
    result = [(arr[i],arr[i]*(i+1)) for i in range(len(arr))]
    result.sort(key=lambda x: x[1])
    final = [i[0] for i in result]
    return final