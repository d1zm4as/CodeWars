


a = ['1', '5', '8', 8, 9, 9, 2, '3'] #11




somaInt = 0
somaStr = 0
for x in a:
    if type(x)==int:
        somaInt+=x
    else:
        somaStr+=int(x)

print(somaInt-somaStr)


