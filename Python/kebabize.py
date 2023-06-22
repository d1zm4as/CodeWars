#s = "SOS"

#s = "42"

#s = 'myCamelCasedString'

s = 'CodeWars'

#s = 'myCamelHas3Humps'

# 1- retirar numeros

# 2 - mudar para caixa baixa

# 3 - adicionar o -

copy = ""

for x in s:
    if x.isdigit():
        pass
    elif x.islower():
        copy+=x
    elif x.isupper():
        a = f"-{x.lower()}"
        copy+=a


if not copy:print("deu")

print(copy.strip("-"))
