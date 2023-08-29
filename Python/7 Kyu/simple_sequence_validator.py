def validate_sequence(arr):
    diff = arr[1]-arr[0]
    
    for x,y in zip(arr,arr[1:]):
        if y-x!=diff:
            return False
    return True