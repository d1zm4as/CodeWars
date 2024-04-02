def popping_blocks(arr):

    stk,popping = [],None
    for v in arr:
        if v==popping: 
            continue
        if stk and stk[-1]==v:
            popping = stk.pop()
        else: 
            stk.append(v)
            popping = None

