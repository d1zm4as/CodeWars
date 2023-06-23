n =3

for _ in range(n):
    print("+"*n)


lista = [("*"*n+"\n") for _ in range(n)]
print(lista)

def generate_shape(n):
    lista = [("+"*n) for _ in range(n)]
    return "\n".join(lista)