def min_sum(arr):
    # Your code here
    pass



#arr = sorted([5,4,2,3])

#arr = sorted([12,6,10,26,3,24])
arr = sorted([9,2,8,7,5,4,0,6])

tam = len(arr)
half= tam//2
a = arr[:half]
b = arr[half:tam][::-1]


soma = 0

for x,y in zip(arr[:half],arr[half:tam][::-1]):
    
    soma+= x*y

print(soma) 

print(sum([(x*y) for x,y in zip (arr[:half],arr[half:tam][::-1])]))
