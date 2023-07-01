abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# chars = ['a','b','c','d','f']
chars = ['O','Q','R','S']

pri = chars[0].lower()
cont = abc.index(pri)
lista = []
for _ in range(len(chars)):
    lista.append(abc[cont])
    
    cont+=1
print(lista)


print(chars)
print(lista)

for x,y in zip(lista,chars):
    cond = True if y.isupper() else False
    if x!=y.lower():
        print(x if not cond else x.upper())

