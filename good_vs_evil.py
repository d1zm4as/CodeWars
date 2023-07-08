def soma_good(s):
    soma = 0
    memog = {1:1,2:2,3:3,4:3,5:4,6:10}
    for idx,x in enumerate(s,start=1):
        t = int(x)
        soma+=t*memog[idx]
    return soma

def soma_evil(s):
    somb = 0
    memoe = {1:1,2:2,3:2,4:2,5:3,6:5,7:10}
    for idx,x in enumerate(s,start=1):
        t = int(x)
        somb+=t*memoe[idx]
    return somb

def good_vs_evil(good, evil):
    if not good:
        return 'Battle Result: Evil eradicates all trace of Good' 
    if not evil:
        return 'Battle Result: Good triumphs over Evil'
    
    a = soma_good(good.split())
    
    b= soma_evil(evil.split())
    
    if a>b:
        return 'Battle Result: Good triumphs over Evil'
    elif b>a:
        return 'Battle Result: Evil eradicates all trace of Good'
    elif a==b:
        return 'Battle Result: No victor on this battle field'
