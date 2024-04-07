def largest_sum(arr):
    if not arr:
        return 0
    
    maior = 0
    
    soma = 0
    
    tam = len(arr)
    
    for i in range(tam):
        soma  = max(arr[i],soma+arr[i])
        maior = max(maior,soma)
    
    return maior