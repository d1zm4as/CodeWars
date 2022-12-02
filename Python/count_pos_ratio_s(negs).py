def count_positives_sum_negatives(arr):
    pos = [x for x in arr if x>0]
    
    neg = sum([y for y in arr if y<0])
    if len(arr)==0:
        return arr
    
    return [len(pos),neg]
