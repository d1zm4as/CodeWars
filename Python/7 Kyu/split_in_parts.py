def split_in_parts(data1, size): 
    arr = [data1[i:i + size] for i in range(0, len(data1), size)]
    return " ".join(arr)