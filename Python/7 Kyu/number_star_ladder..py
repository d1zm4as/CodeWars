def pattern(n):
    if n==1:
        return "1"
    copy = "1\n"
    for  x in range(2,n+1):
        a = x-1
        copy+=str(1)
        copy+="*"*a
        copy+=str(x)
        if x == n:
            break
        copy+="\n"
    return copy