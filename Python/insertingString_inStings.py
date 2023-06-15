# frase = "I like codewars! It makes me happy."
# t = " really"
# a = [1, 28]
frase = "'I' write a wi said Phi"
t = "ll"
a = [3,14,24] 

lista = []
for idx,x in enumerate(frase):
    print(idx,x)
    if idx in a:
        lista.append(f"{t}")
    lista.append(x)


copy = "".join(lista)
print(copy)
if max(a)>len(frase):
    copy+=t
print(copy)


