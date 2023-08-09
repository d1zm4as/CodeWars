def to_underscore(s):
    if str(s).isdigit():
        return str(s)
    copy= ""
    copy+=s[0].lower()
    for x in  s[1:]:
        if x.isupper():
            copy+="_"
            copy+=x.lower()
        else:
            copy+=x
#     return "_".join(copy.split())
    return copy