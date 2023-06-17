def fib(n,memo = {}):
    if n<2:return 1
    if n in memo: return memo[n]
    memo[n] = fib(n-1)+fib(n-2)
    return memo[n]


def solve(n):
    soma = 0
    for x in range(n+1):
        soma+=fib(x)
    
    return soma*4


print(solve(5)==80)
print(solve(7)==216)
print(solve(20)==114624)




