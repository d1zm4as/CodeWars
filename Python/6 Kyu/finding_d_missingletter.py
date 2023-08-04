def find_missing_letter(chars):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    pri = chars[0].lower()
    cont = abc.index(pri)
    lista = []
    for _ in range(len(chars)):
        lista.append(abc[cont])

        cont+=1

    for x,y in zip(lista,chars):
        cond = True if y.isupper() else False
        if x!=y.lower():
            return x if not cond else x.upper()  