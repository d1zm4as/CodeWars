from statistics import Counter 
def flatten(array):
    return sorted([y.lower() for x in set(array) for y in x])

def find_uniq(s):

    arr = flatten(s)

    a = Counter(arr)

    menos = min(a,key = arr.count)

    for x in set(s):
        if menos in x:
            return x
    return "Harry Potter"