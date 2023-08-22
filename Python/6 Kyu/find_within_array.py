def find_in_array(seq, predicate): 
    lista = []
    cont = 0
    for idx,x in enumerate(seq):
        if predicate(x,idx):
            return idx
    return -1
