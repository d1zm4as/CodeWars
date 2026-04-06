from collections import Counter
def odd_ones_out(numbers):
    lista = []
    
    a = Counter(numbers)
    
    for x in numbers:
        if a[x] % 2==0:lista.append(x)
    return lista