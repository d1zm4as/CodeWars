from statistics import Counter 
s = [ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]
s = [ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]
def flatten(array):
    return sorted([y.lower() for x in set(array) for y in x])


arr = flatten(s)
print(arr)
a = Counter(arr)

print(a)
menos = min(a,key = arr.count)

for x in set(s):
    if menos in x:
        print(x)