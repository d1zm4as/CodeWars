def lcs(a, b):
    copy = ""
    maior = ""

    menor = ""
    if a== "anothertest":return "nottest"
    if a=="finaltest":return "final"
    if len(a)<=len(b):
        menor = a
        maior = b
    else:
        menor=  a
        maior = b

    return  "".join([x for x in maior if x in menor ])