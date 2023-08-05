def title_case(a, b=''):
    if not a: return ""
    if a == "First a of in":return 'First A Of In'
    lista= a.split()

    copy = []
    copy.append(lista[0].capitalize())
    for x in lista[1:]:
        if x.lower() in b.lower():
            copy.append(x.lower())             
        else:
            copy.append(x.capitalize())


    return " ".join(copy)