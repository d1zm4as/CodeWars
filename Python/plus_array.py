def up_array(arr):
    copy = ""
    if not arr:
        return None
    if arr == [0]:
        return [1]
    
    for idx,x in enumerate(arr):
        if idx>0 and x<0:
            return None
        elif len(str(x))>1:
            return None
        else:
            a = str(x)
            copy+=a
    
    soma = int(copy)+1
    turn = ""
    qtd = 0
    if arr[0] ==0 :
        qtd+=1
        if arr[1]==0:
            qtd +=1
    
    if arr[0]==0:
        turn+="0"*qtd
        turn+=str(soma)
        return [int(x) for x in turn]
    turn +=str(soma)
    return [int(x) for x in turn]
    