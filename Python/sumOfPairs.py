# s = 6
# ints = [4, 3, 2, 3, 4]

ints = [10, 5, 2, 3, 7, 5]
s = 10


cache = set()
for i in ints:
    print(i)
    if s - i in cache:
        print([s - i, i])
    cache.add(i)


print(cache)