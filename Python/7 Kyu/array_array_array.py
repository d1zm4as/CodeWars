def explode(x):
    if isinstance(x[0], int) and isinstance(x[1], int):
        score = x[0] + x[1]
    elif isinstance(x[0], int):
        score = x[0]
    elif isinstance(x[1], int):
        score = x[1]
    else:
        return 'Void!'
    
    return [x] * score