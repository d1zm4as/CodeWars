def reverse_number(n):
    sign = -1 if n<0 else 1
    
    n = abs(n)
    
    n = str(n)
    
    n = int(n[::-1])
    return n*sign