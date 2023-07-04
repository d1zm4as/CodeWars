from gmpy2 import is_prime

def check(x):
    a = str(x)
    if not is_prime(x) :return False
    
    for y in a:
        if int(y)%2==0:
            return False
    return True

n = 55

lista=  []

for x in range(1,n):
    if check(x):
        lista.append(x)
adj = 0
cont = n
while True:
    if check(cont):
        adj = cont
        break
    else:
        cont+=1
print(lista)
print([len(lista),max(lista),adj])
