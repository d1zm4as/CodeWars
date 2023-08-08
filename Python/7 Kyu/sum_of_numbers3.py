

def get_sum(a,b):
    ref = [a,b]
    if a ==b:
        return a
    diff = 0
    for x in range(min(ref),max(ref)+1):
        diff+=x
    
    return diff

