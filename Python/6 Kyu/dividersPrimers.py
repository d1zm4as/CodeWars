# Don't forget to sort your result list!
def get_dividers(values, powers):
    total = []
    for x,y in zip(values,powers):
            total.append(x**y)


    prod = 1
    for x in total:
        prod*=x


    lista = sorted([x for x in range(1,prod+1) if prod%x==0])

    return lista