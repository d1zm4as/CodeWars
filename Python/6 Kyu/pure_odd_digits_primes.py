from gmpy2 import is_prime

def check(x):
    a = str(x)
    if not is_prime(x) :return False
    
    for y in a:
        if int(y)%2==0:
            return False
    return True



def only_oddDigPrimes (n): # P.O.D.P (pure ood digit prime)
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
    return [len(lista),max(lista),adj]
