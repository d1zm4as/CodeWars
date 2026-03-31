def solve(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '01'
    else:
        a, b = '0', '01'
        for i in range(2, n + 1):
            a, b = b, b + a
        return b