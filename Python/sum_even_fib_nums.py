def SumEvenFibonacci(m):
    x,y = 1, 2
    counter = 0
    while y <= m:
        if y % 2 == 0:
            counter += y
        x,y = y, x+ y
    return counter