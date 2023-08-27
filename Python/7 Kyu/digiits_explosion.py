def explode(s):
    copy  = ""
    
    for x in s:
        if x != "0":
            copy += int(x)*x
    return copy