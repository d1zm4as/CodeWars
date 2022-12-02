

def series_sum(n):
    if n ==0:
        return "0.00"
    if n ==1:
        return "1.00"
    lol = 1
    
    soma = 1
    for x in range(1,n):
        lol+=3
        soma += 1/lol
    
    
    return f"{round(soma,2):.2f}"

