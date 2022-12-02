

def printer_error(s):
    lista = [x for x in s if x not in "abcdefghijklm"]
    
    return f"{len(lista)}/{len(s)}"

