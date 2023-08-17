def ok(n):
    return sum(int(x)**2 for x in str(n))

def square_digits_sequence(n):
    cont = 0
    ant = n
    lista = [n]
    while True:
        total = ok(ant)
        if total in lista:
            break
        
        ant = total
        lista.append(total)
        cont+=1
    return cont+2

