
values  = [5,7,11]

powers = [2,1,1]

total = []
for x,y in zip(values,powers):
        total.append(x**y)


prod = 1
for x in total:
    prod*=x

print(prod)

lista = sorted([x for x in range(1,prod+1) if prod%x==0])

print(lista)