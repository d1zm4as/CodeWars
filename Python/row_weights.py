

soma1 = 0

soma2 = 0

lista = [70,58,75,34,91]

for idx,x in enumerate(lista):
    if idx%2==0:
        soma1+=x
    else:
        soma2+=x

print([soma1,soma2])

