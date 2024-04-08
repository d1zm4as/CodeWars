def mine_location(arr):


    res = [0,0]

    for x in arr:
        if 1 in x:
            res[1] = x.index(1)
            return res
        else:
            res[0]+=1