def check(arr,k):
    for x in k:
        if x not in arr:
            return False
    return True



def killer(suspect_info, dead):
    for x in suspect_info:
        a = suspect_info[x]
        if check(a,dead):
            return x
    