def first_n_smallest(lst, n):
    sorted_lst = sorted(lst)
    smallest_elements = sorted_lst[:n]
    result = []
    
    for element in lst:
        if element in smallest_elements:
            result.append(element)
            smallest_elements.remove(element) 
    return result