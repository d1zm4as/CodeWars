a  = "111000" 
b = "000110" 
n = 3


print(a[n:])

copya = a[:n]+b[n:]
copyb = b[:n]+a[n:]

print([copya,copyb])