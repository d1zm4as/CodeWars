from collections import Counter
def duplicate_encode(word):
    lista = ""
    a = word.lower()
    lol = Counter(a)
    for x in a:
        if lol[x]==1:
            lista+="("
        if lol[x]>1 :
            lista+=")" 
    return lista
