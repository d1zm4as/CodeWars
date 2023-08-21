def replace_nth(text, n, old, new):
    copy = ""
    cont = 0
    for x in text:
        if x == old:
            cont+=1
            if cont==n:
                copy+=new
                cont = 0
                continue
        copy+=x
        
    return copy