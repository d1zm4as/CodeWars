arr = [1,3,5,7]

a = 3

b = 1



for x,y in zip(arr,arr[1:]):
    if x==a and y==b or x==b and y==a:
        print(True)
    
print(False)
