def password(string):
    if len(string)<8:
        return False
    cond1 = False
    cond2 = False
    cond3 = False    
     
    for x in string:
        if x.islower():
            cond2 = True
        if x.isupper():
            cond1 = True
        if x.isdigit():
            cond3 = True
    return cond1 and cond2 and cond3