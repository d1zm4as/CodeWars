from statistics import Counter

def scramble(s1,s2):
    a = Counter(s1)

    b =Counter(s2)

    lista = []
    for x in s2:
        if b[x]<=a[x]:
            lista.append(x)
    return len(lista)==len(s2)