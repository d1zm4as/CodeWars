def word_search(s, array):
  
    if not s:
        return array
    lista = []
    for x in array:
        if s.lower() in x.lower():
            lista.append(x)
    
    if len(lista)==0:
        return ["None"]
    return lista