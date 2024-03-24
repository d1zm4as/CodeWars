def string_expansion(s):
    if not s:
        return ""
    

    ref = set(["0","1","2","3","4","5","6","7","8","9"])
    copy = ""
    
    ant = s[0]
    if ant not in ref:
            copy+=ant

    for x in s[1:]:

        
        if x in ref and ant in ref : # se ant e x forem numeros
            ant = x
        if ant not in ref and x in ref: # se ant nao esta em ref e x esta
            ant  = x 
        if ant in ref and x not in ref: # se só ant for numero
                copy+=x*int(ant)
        if not ant in ref and  not x in ref: # se dois nao foram num
                copy+=x

    return copy 