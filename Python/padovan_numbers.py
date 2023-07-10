def padovan(n,memo = {}):
    if n ==0:return 1
    if n ==1:return 1
    if n==2:return 1
    if n in memo:return memo[n]
    memo[n] = padovan(n-2)+padovan(n-3)
    return memo[n]