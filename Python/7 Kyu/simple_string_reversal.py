s = "our code"
s = "your code rocks"
lista = []

copy = []
for idx,x in enumerate(s):
    if x == " ":
        lista.append(idx)
    else:
        copy.append(x)
print(lista)
copy = copy[::-1]
print(copy)
for x in lista:
    copy.insert(x," ")
print(copy)
print("".join(copy))


