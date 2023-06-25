from itertools import chain, combinations
def powerset(items):
    l_items = list(items)
    return chain.from_iterable(combinations(l_items, r) for r in range(len(l_items) + 1))
xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

# lim,n = 230,4

# lim,n = 430,5

lim,n = 430,8



# print(max([sum(x) for x in list(powerset(xs)) if sum(x) <=lim] ))

lista = [sum (x) for x in combinations(xs, n) if sum(x)==lim]

for x in lista:
    print(x)