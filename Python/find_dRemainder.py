def remainder(a,b):
    if min(a,b) == 0:
        return None
    elif a > b:
        return a % b
    else: 
        return b % a