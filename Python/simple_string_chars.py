def solve(s): 
    up = 0 
    low = 0 
    nums = 0 
    xs = 0 
    for x in s: 
        ref = ord(x) 
        if ref>=65 and ref <=90: up+=1 
        elif ref>=97 and ref <=122: low+=1 
        elif x.isdigit(): nums+=1 
        else: xs+=1
    lista = [up,low,nums,xs] 
    return lista
