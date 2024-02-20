def absent_vowel(x): 
    lista = set(list(x.lower()))
    if "a" not in lista:
        return 0
    if "e" not in lista:
        return 1
    if "i" not in lista:
        return 2
    if "o" not in lista:
        return 3
    if "u" not in lista:
        return 4