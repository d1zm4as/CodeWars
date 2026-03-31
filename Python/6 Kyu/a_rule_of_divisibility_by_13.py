def thirt(n):
    restos  = [1,10,9,12,3,4]
    total = 0
    for i in range(len(str(n))):
        total += int(str(n)[-1-i]) * restos[i%6]
    if total == n:
        return total
    else:        return thirt(total)


print(thirt(1234567)) # 87
print(thirt(321)) # 48
print(thirt(8529)) # 79
print(thirt(85299258)) # 31     