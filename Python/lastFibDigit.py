def last_fib_digit(n):
    """ Os ultimos numeros duma sequencia fibonacci se repetem a cada 60 casos """
    a = 0
    b = 1
    for _ in range(n%60):
        a, b = b, (a+b)%10
    return a

