# from gmpy2 import factorial
def factorial(x):
    total = 1
    
    for x in range(1,x+1):
        total*=x
    return total

def sum_factorial(lst):
    return int((sum(factorial(x) for x in lst)))