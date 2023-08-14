import gmpy2 #pip install gmpy2

def fib(n):
    return gmpy2.fib(abs(n)) * (-1 if n < 0 and n % 2 == 0 else 1)



print(fib(77)) 

# def fib(n):
#   """I love this solution from SICP and have been 
#   practicing it from memory for the last year.
#   """
#   a, b, p, q = 1, 0, 0, 1
#   sign = -1 if (n < 0) & (abs(n) % 2 == 0) else 1
#   n = abs(n)
#   while True:
#       if n == 0:
#           return b * sign
#       elif n % 2 == 0:
#           p, q = (p**2 + q**2), (q**2 + 2*p*q)
#           n /= 2
#       else:
#           a, b = (b*q + a*q + a*p), (b*p + a*q)
#           n -= 1