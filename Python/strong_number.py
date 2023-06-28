def fact(n):
    total = 1

    for x in range(1,n+1):
        total*=x
    return total



# n = 145
# n = 2
# n = 1

# n=7
# n=93
n=185

soma = sum(fact(int(x)) for x in str(n))


print(soma==n)

