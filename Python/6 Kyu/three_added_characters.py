from collections import Counter

def added_char(s1,s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    diff = c2 - c1
    for x in diff:
        if diff[x] ==3:
            return x