s = "the-stealth-warrior"
s = 'the_stealth_warrior'
s = s.replace("-", ",")
s = s.replace("_", ",")
lista = [x for x in s.split(",")]

print(lista)

copy = lista[0]

for x in lista[1:]:
    copy+=x.capitalize()
print(copy)



