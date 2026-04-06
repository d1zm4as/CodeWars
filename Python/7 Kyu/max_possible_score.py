def max_possible_score(points, seen): 
    # your code here
    soma = 0
    if seen:
        for x in seen:
            if x in points:
                points[x] += points[x]
    
    for x in points:
        soma+=points[x]
    return soma