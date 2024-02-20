def tr(n):
    s = str(n)
    copy = ""
    memo = {"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
    for x in s:
        copy+=memo[x]
    return copy




def numbers_of_letters(n):
    lista = []

    x = tr(n)
    lista.append(x)
    while x!="four":
        aux = len(x)
        x = tr(aux)
        lista.append(x)

    return lista