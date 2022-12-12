def delete_nth(lista,m):
    mopa = []
    for x in lista:
        if mopa.count(x)<m:
            mopa.append(x)
    return mopa
