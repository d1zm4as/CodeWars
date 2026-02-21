#longest alphabetical substring

def longest(s):
    lista = []
    copy = ""
    item =  s[0]
    for x in s:
        if ord(x) >= ord(item):
            copy += x
        else:
            lista.append(copy)
            copy = x
        item = x
    lista.append(copy)
    return max(lista, key=len)