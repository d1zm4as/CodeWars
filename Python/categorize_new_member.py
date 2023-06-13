

a = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]


lista =[] 

for x in a:
    if x[0]>=55 and x[1]>7:
        lista.append("Senior")
    else:
        lista.append("Open")

print(lista)

print(["Senior" if x[0]>=55 and x[1]>7 else "Open" for x in a ])




