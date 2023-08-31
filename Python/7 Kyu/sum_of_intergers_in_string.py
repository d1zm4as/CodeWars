def sum_of_integers_in_string(s):
    lista = []
    
    copy = ""
    s = s.replace(" ","")
    for x in s:

        if x.isnumeric():
            copy+=x
        else:
            lista.append(copy)        # lista.append(int(copy))
            copy = ""
    lista.append(copy)  
    return sum([int(x) for x in lista if x.isdigit()])

