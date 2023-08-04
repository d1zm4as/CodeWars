def order(a):
    lol = [(x,i) for i in range(1,10) for x in a.split() if str(i) in x]
    
    return " ".join([x[0]for x in lol])
