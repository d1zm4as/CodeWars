def check(a):
    t = 1
    idx= 1
    for x in str(a):
        t+= int(x)**idx
        idx+=1
    return a == t-1

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    return [x for x in range(a,b+1) if check(x)]
