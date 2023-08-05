
s = "Reverse this string, please!"
r = "Reverse siht string, !esaelp"
s  ="Did it work?"

lista = []




for idx,x in enumerate(s.split()):

    if idx%2==0:
        lista.append(x)
    else:
        lista.append(x[::-1])

print(lista)
print(" ".join(lista))
