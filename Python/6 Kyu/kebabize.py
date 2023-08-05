def kebabize(s):
    copy = ""

    for x in s:
        if x.isdigit():
            pass
        elif x.islower():
            copy+=x
        elif x.isupper():
            a = f"-{x.lower()}"
            copy+=a


    if not copy: return ""
    
    return copy.strip("-")

