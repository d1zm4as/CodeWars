from statistics import Counter
def only_duplicates(string):
    a = Counter(string)
    copy = ""
    for x in string:
        if a[x]>1:
            copy+=x
    return copy