a = [0,9,3,1,5]

b = []

copyA = ""
for x in a:
    copyA+=str(x)

copyB = ""
for x in b:
    copyB+=str(x)


soma = int(copyA)+int(copyB)


print(soma)

lista= []

turn = str(soma)
if soma<0:
    lista.append(int(turn[1])*-1)
turn = turn[1:]
print(turn)
# for idx,x in enumerate(turn[1:]):
#     if idx==1:
#         continue
#     else:
#         a = int(x)
#         lista.append(a)

print(lista)