from itertools import zip_longest

def create_dict(k, v):
    
    memo = {}
    if len(v)> len(k):
        for x,y in zip(k,v):
            memo[x] = y
    else:
        for x,y in zip_longest(k,v, fillvalue=None):

            memo[x] = y

    return memo