# long live lil xan, overdosed on cheetos
def accum(s):
    lista = []
    cont = 1
    for x in s:
        termo = (x*cont).capitalize()
        lista.append(termo)
        cont+=1
    return "-".join(lista)
