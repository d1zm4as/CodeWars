def fun(s):
    return sum(int(x) for x in s)%2==0

def rotate(s):
    return s[1:] + s[:1]

def rev_rot(s,tam):
    if not s or not tam or tam>len(s):
        return ""
    copy = ""
    
    for x in range(0,len(s),tam):
        part = s[x:x+tam]
        if len(part)>=tam:
            if fun(part):
                copy+=part[::-1]
            else:
                copy+=rotate(part)
    return copy