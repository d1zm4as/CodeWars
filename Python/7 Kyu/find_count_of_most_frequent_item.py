from collections import Counter
def most_frequent_item_count(c):
    if not c:
        return 0
    a = Counter(c)
    item = c[0]
    maior = a[item]
    
    for x in c:
        if a[x]>maior:
            item  = x
            maior = a[x]
    return maior