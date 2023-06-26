s,r = "String",'StRiNg'

s,r = "Weird string case",'WeIrD StRiNg CaSe'

lista= []
for x in s.split():
    copy = ""  
    for idx,y in enumerate(x):
        if idx%2==0:
            copy+=y.upper()
        else:
            copy+=y.lower()
    lista.append(copy)



print(lista)
lista = " ".join(lista)
print(lista==r)




