def positive_sum(arr):
    return 0 if len(arr)==0 else sum([x for x in arr if x>0])
