arr = [16,17,14,3,14,5,2]#[ 17,14,5,2]

lista = []

tam = len(arr)

cont = 0

while cont < tam:
    atual  = arr[cont]
    ref = max(arr[cont:])
    if atual>=ref and atual not in lista:
        lista.append(atual)
    print(atual,"---",ref)
    cont+=1

print(lista)