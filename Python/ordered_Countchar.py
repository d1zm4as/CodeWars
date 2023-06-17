def func(x):
    return x[1]
 
s = "abracadabra"
# copy = set(s) # set nao mantem a ordem inicial


#lista = [(x,s.count(x))for x in copy]


copy = []
for x in s:
    if x not in copy:
        copy.append(x)

print(copy)

lista = [(x,s.count(x))for x in copy]
print(lista)



