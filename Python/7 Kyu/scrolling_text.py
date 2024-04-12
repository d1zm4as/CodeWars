def scrolling_text(text):
    text = text.upper()
    lista = []
    for x in range(len(text)):
        lista.append(text[x:]+text[:x])
    return lista