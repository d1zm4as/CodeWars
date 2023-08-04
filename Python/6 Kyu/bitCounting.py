n = 1234


print(bin(n))

lista = [ int(x) for x  in str(bin(n))[2:]]

print(sum(lista))


print(bin(n).count('1'))