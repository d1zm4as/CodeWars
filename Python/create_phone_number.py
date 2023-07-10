def create_phone_number(n):
    arr = [str(x) for x in n]
    copy = ""
    copy+="("
    pri = "".join(arr[:3])
    copy+=pri+")"+" "
    
    mid = "".join(arr[3:6])
    copy+=mid+"-"
    fim = "".join(arr[6:])
    copy+=fim
    return copy

