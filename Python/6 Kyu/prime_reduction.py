from gmpy2 import is_prime 

def digit_prod_sum(n):
    return sum( int(d)**2 for d in str(n) )
        

def solve(a,b):
    count = 0
    for n in range(a, b):
        if is_prime(n):
            i = n
            while i > 9:
                i = digit_prod_sum(i)
            if i in [0, 1, 7]:
                count += 1
            
    return count 

    