

def alphabet_position(text):
    tam = [x for x in text]
    string = "abcdefghijklmnopqrstuvwxyz"
    lista = [x for x in string.lower()]
    beto = []
    a = ""
    for x in text.lower().strip():
        if x in string:
            indexo = lista.index(x)+1
            beto.append(f"{str(indexo)} ")
    
    lol = "".join(beto)
    pop = lol.strip()
    
    return pop

