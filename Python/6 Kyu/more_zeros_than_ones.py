from collections import Counter
def more_zeros(s):
    lista = []
    seen = set()
    for x in s:
        
        if x not in seen:
            a = bin(ord(x))[2::]

            b = Counter(a)

            if b["0"]>b["1"]:
                lista.append(x)
        
            seen.add(x)            
    return lista