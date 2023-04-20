def find_multiples(integer, limit):
    return [x for x in range(1,limit+1) if x%integer==0]
