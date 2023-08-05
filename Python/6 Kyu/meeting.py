def sep(s):
    arr = []
    for x in s.upper().split(";"):
        idx = x.index(":")
        last = x[:idx]
        pri = x[idx+1:]
        arr.append((pri,last))
    return arr

def turn(arr):
    copy = ""
    for x in arr:
        copy+="("
        copy+=x[0]
        copy+=","
        copy+=" "
        copy+=x[1]
        copy+=")"
    return copy

def meeting(s):
    lista = sep(s)
    lista = sorted(lista)
    a = turn(lista)
    return a
