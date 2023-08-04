from collections import Counter
def top_3_words(text):
    """"
    lista = Counter(x for x in text.lower().split()if x not in"#@/$%¨&...*(),.")
    
    return [x for x,_ in lista.most_common(3)]
    
    """
    for c in text:
        # if it's not alphanumeric or an apostrophe
        if not (c.isalpha() or c=="'"):
            # replace with a space
            text = text.replace(c,' ')
    lista = [ x for x in text.lower().split()if x not in"#@/'''$%¨&...*(),."]
    
    if len(lista)<3 :
        
        top = Counter(lista)
        return [x for x,_ in top.most_common(len(lista))]
    top = Counter(lista)
    return [x for x,_ in top.most_common(3)]
