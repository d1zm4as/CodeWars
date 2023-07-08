s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"

r  = "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"

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

lista = sep(s)
print(lista)
lista = sorted(lista)
print(lista)
a = turn(lista)
print(a)
print(r)
print(a==r)