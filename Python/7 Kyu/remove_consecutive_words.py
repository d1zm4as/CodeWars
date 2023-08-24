def remove_consecutive_duplicates(s : str) -> str:
    if not s:
        return ""
    arr = s.split()
    lista = [arr[0]]
    
    for x in arr[1:]:
        if x != lista[-1]:
            lista.append(x)
        
    return " ".join(lista)