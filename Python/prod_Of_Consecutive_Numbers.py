


"""
n = 0
while n<1000:
    print(f"Test Case - {n}")
    lista = [fib(x) for x in range(len(str(n))*5)]
    lista[0]=0

   
    for x,y in zip(lista,lista[1:]):
        if x*y ==n:
            print([x,y,True])
            break
        if x*y>n :
            print([x,y,False])
            break
    n+=1

"""
"""
n = 7

lista = [fib(x) for x in range(len(str(n))*6)]
lista[0]=0
print(lista)
for x,y in zip(lista,lista[1:]):
    if x*y ==n:
        print([x,y,True])
        break
    if x*y>n :
        print([x,y,False])
        break

"""
n = 4895

x = 0
y = 1

while n>x*y:
    x,y = y,y+x
print([x,y,n==x*y])