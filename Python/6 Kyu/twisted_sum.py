def soma(n):
    a = str(n)
    return sum(int(x) for x in a)



def compute_sum(n):
    total = 0
    for x in range(1,n+1):
        if x <10:
            total+=x
        else:
            total+= soma(x)
    return total