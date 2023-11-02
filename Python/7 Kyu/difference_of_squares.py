def difference_of_squares(n):
    soma = 0
    somb = 0
    for x in range(n+1):
        soma += x
        somb +=x*x
        
    return soma**2 -somb