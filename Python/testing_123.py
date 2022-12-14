def number(lines):
    if lines:
        lista = []
        for idx,x in enumerate(lines,start=1):
            lista.append(f"{idx}: {x}")
        return lista
    else:
        
        return []
