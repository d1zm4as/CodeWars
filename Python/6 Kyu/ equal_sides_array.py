arr = [1,2,3,4,3,2,1]
arr =[1,100,50,-51,1,1]
arr = [-1,-2,-3,-4,-3,-2,-1]
arr =[-1,-2,-3,-4,-3,-2,-1]
arr = [-17, 15, 3, 20, 13, -6, -20, -16, 8]
arr = [20,10,-80,10,10,15,35]
arr = [10,-80,10,10,15,35,20]
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1
