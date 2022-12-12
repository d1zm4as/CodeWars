def tourney(inp):
    res = [inp]
    temp = []
    while len(inp) > 1:
        for i in range(0, len(inp), 2):
            if i+1 == len(inp):
                temp.insert(0, inp[i])
            else:
                temp.append(max(inp[i], inp[i+1]))
        inp = temp
        res.append(temp)
        temp = []
    return res
        
