def highest_rank(a):
    maior = max([a.count(x) for x in set(a)])
    lista = max([x for x in set(a) if a.count(x)==maior])
    return lista