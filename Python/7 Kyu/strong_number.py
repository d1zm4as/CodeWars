def fact(n):
    total = 1

    for x in range(1,n+1):
        total*=x
    return total


def strong_num(n):
    soma = sum(fact(int(x)) for x in str(n))
    if soma==n:
        return "STRONG!!!!"
    return "Not Strong !!"