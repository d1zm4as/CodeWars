from statistics import Counter
def repeats(arr):
    a = Counter(arr)
    return sum([x for x in arr if a[x]==1])


print(1080-976)