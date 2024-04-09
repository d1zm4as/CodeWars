# 1+1 = 1 e sobra 1
# 1+0 = 1
# 0+1 = 1 
# 0+0 = 0

def bin_add(a,b):
    maior = max(len(a),len(b))

    a = a.zfill(maior)
    b = b.zfill(maior)

    copy = ""

    add1 = 0

    for i in range(maior-1,-1,-1):
        soma = add1
        soma +=1 if a[i] == "1" else 0
        soma+=1 if b[i] == "1" else 0
        copy = ('1' if soma%2 ==1 else '0')+copy
        add1 = 0 if soma<2 else 1
    if add1!=0:copy = '1'+copy

    return copy.zfill(maior)




def add(a,b):
    a = bin_add(a,b)
    a = a.lstrip('0')
    return a if len(a)>0 else "0"