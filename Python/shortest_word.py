def find_short(s):
    # your code here
    return min([len(x) for x in s.split() if x!=" "])
