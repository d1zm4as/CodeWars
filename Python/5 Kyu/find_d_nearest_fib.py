num = 2**512
# if (num == 0):
    
#     return 0

first = 0
second = 1

third = first + second

while (third <= num):
    
    first = second

    second = third

    third = first + second
   
if (abs(third - num) >=
    abs(second - num)):
    ans = second
else:
    ans = third

print(ans)
print(cont)