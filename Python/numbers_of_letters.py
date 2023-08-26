def numbers_of_letters(n):
    a  = str(n)
    lista = []
    copy = "".join([memo[x] for x in a])
    if copy == "four":
        return [copy]
    lista.append(copy)
    
    tam = str(len(copy))
    while memo[tam]!='four':
        ref = memo[tam]
        lista.append(ref)
        tam = str(len(ref))


    lista.append('four')
    return lista
