num = 564
# num = 89


def check(num):
    cont = 1
    soma = 0
    for x in [int(x) for x in str(num)]:
        soma+= x**cont
        cont+=1
    return soma==num


def disarium_number(number):
    return "Disarium !!" if check(number)else "Not !!"
