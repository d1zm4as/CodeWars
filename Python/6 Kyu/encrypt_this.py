def sosa(s):
    if not s:return ""   
    copy = ""

    pri = str(ord(s[0]))
    if len(s)==1:
        return pri
    seg = s[1]

    tam = len(s)-1
    ul = s[tam]

    for idx,x in enumerate(s):
        if idx == 0:
            copy+=pri
        elif idx ==1:
            copy+=ul
        elif idx == tam:
            copy+=seg
        else:
            copy+=x
    return copy

def encrypt_this(s):
    lista = [sosa(x) for x in s.split()]
    
    return " ".join(lista)