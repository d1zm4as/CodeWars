def max_sequence(arr):
    maior = 0
    
    soma = 0
    
    tam = len(arr)
    
    for i in range(tam):
        soma  = max(arr[i],soma+arr[i])
        maior = max(maior,soma)
    
    return maior
