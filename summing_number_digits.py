def sum_digits(a):
    if a <0:
        a = a*-1
        return sum([int(x)for x in str(a)])
    else:
        return sum([int(x)for x in str(a)])