
def longest_consec(arr, k):
    if len(arr) == 0 or k>len(arr) or k<=0:
        return ""
    else:
        lista = []
        for x in range(0,len(arr)):
            a  =''.join(arr[x:x+k])
            lista.append(a)
        return max(lista,key=len)