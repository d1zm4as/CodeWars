def word_to_bin(word):
    lista = []
    for x in word:
        a = bin(ord(x))[2:]
        lista.append(a.zfill(8))
    return lista