
def fib(n,memo = {}):
    if n in memo:return memo[n]
    if n<=2:return 1
    memo[n] = fib((n-1))+fib((n-2))
    return memo[n]
    

def perimeter(n):
    if n == 0: return 4
    h = fib(n+1)
    l = fib(n)+h
    return 2*h+2*l
    