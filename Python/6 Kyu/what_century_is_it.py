def what_century(s):
    co = int(s[:2])
    final = int(s[2:])
    memo = {"1":"st","2":"nd","3":"rd"}
    
    lol = True if int(s)<1500 else False
    
    if final >0:
        aux = str(co+1)
        if lol:
            return aux+"th"
            
        if aux[-1] in memo:
            return aux+memo[aux[-1]]
        else:
            return aux+"th"

    if final ==0:
        aux = str(co)
        if lol:
            return aux+"th"
        
        if aux[-1] in memo:
            return aux+memo[aux[-1]]
        else:
            return aux+"th"
