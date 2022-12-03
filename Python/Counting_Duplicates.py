from collections import Counter
def duplicate_count(text):
    cont,a = 0, Counter(text.lower())
    
    for x in a:
        if a[x]>=2:
            cont+=1
            
    return cont
