from collections import Counter

def find_added(s, r):
    a = Counter(s)
    b = Counter(r)

    lista=  []

    for x in set(r):
        if x in set(s):
            tam =  (b[x]-a[x])*x
            lista.append(tam)
        else:
            tam =  b[x]*x
            lista.append(tam)


    return "".join(sorted(lista))

from collections import Counter

def findAdded(st1, st2):
    return ''.join(sorted((Counter(st2) - Counter(st1)).elements()))