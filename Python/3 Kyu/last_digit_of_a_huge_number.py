def last_digit(lst):
    n = 1
    for x in lst[::-1]:
        termo = n if n < 4 else n % 4 + 4
        n = pow(x,termo)
    return n % 10