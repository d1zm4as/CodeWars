def fib(n,memo = {}):
    if n in memo:return memo[n]
    if n<=2:return 1
    memo[n] = fib((n-1))+fib((n-2))
    return memo[n]
    

n = 5

h = fib(n+1)

l = fib(n)+h

print(2*h)

print(2*l)

