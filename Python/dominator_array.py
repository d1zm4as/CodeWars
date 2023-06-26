arr = [3,4,3,2,3,1,3,3]

size = len(arr)/2

for x in set(arr):
    if arr.count(x)>size:
        print(x)

print(-1)
