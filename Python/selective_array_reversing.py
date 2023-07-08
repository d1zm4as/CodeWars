def flatten(array):
    return [y for x in array for y in x]        


arr = [2,4,6,8,10,12,14,16]


l = 3

lista = [sorted(arr[i:i + l],reverse=True) for i in range(0, len(arr), l)]

arr = [flatten(lista)]

print(arr)