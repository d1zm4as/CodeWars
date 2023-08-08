def triple_x(s):
    cont = 0
    tam = len(s)
    while cont<tam-2:
        if s[cont]=='x':
            if s[cont+1]=='x' and s[cont+2]=='x':
                return True
            return False
        cont+=1
    
    return False
    