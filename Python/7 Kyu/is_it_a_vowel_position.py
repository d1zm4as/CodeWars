def check_vowel(s, p):
    
    if p<0 or p> len(s):
        return False
    lista = set(["a","e","i","o","u","A","E","I","O","U"])
    return s[p] in lista