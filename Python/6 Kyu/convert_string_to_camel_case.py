def to_camel_case(s):
    s = s.replace("-", ",")
    s = s.replace("_", ",")
    lista = [x for x in s.split(",")]


    copy = lista[0]

    for x in lista[1:]:
        copy+=x.capitalize()
    return copy
