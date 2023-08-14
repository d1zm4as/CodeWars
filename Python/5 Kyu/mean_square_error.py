def solution(a,b):
    soma = 0
    tam = len(a)
    cont = 0
    while cont< tam:
        diff = abs(a[cont]-b[cont])
        soma += diff*diff
        cont+=1
    return soma/cont