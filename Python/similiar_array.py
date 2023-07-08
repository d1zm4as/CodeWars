arr1 = [1, 2, 3, 4]
arr2 = [1, 2, 3, "4"]

def arrays_similar(seq1, seq2): 
    if len(seq1)>len(seq2) or len(seq2)>len(seq1):
        return False
    
    for x in set(seq1):
        if x in seq2:
            if seq1.count(x)!=seq2.count(x):
                   return False
        else:
            return False
    return True