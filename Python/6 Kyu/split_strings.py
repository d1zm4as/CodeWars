def solution(s):
    size = len(s)
    lista = []
    if not s:
        print("")

    if size%2!=0:

        s+="_"
        lista= [s[i:i+2] for i in range(0,size,2)]
    else:
        lista= [s[i:i+2] for i in range(0,size,2)]


    return lista