def solution(number):
    soma = 0
    
    for x in range(number):
        if x%3==0 or x%5==0:
            soma+=x
    return soma
