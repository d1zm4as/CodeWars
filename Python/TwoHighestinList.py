def two_highest(arg1):
    if not arg1:
        return []
    if len(set(arg1))==1:
        return [arg1[0]]
    maior = max(arg1)
    smaior = max([x for x in arg1 if x!= maior])
    return[maior,smaior]




lista = [15,20,20,17]


print(two_highest(lista))



