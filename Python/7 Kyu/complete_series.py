def complete_series(seq): 
    if len(set(seq)) !=len(seq):return [0]
    
    return list(range(max(seq)+1))