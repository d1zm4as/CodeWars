from itertools import chain, combinations
def powerset(items):
    
    l_items = list(items)
    return chain.from_iterable(combinations(l_items, r) for r in range(len(l_items) + 1))
def choose_best_sum(lim, n, xs):
    if not xs:return None
    lista = [sum (x) for x in combinations(xs, n) if sum(x)<=lim]
    if not lista:return None
    return max(lista)
