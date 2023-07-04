from gmpy2 import is_prime

def check(x):
    
    cont= 0 
    for y in str(x):
        if int(y)%2==0:
            cont+=1
    return cont


n = 487

ref = n-1




maior = 0
lol = 0
for x in range(ref,0,-1):
    if is_prime(x):
        a =check(x)
        if a>maior:
            maior = a
            lol = x
        if maior>len(str(x)):
            break


print(f"{lol} == {maior}")


