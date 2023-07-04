arr = [1,2,6,1,6,3,1,9,6]
arr  = [1,2,2,1,6,1,3,9,6,1]
arr = [1,2,3]

soma = 0
for idx,x in enumerate(arr):
    if idx%2==0:
        soma+= x
    else:
        soma*=x

print(soma)