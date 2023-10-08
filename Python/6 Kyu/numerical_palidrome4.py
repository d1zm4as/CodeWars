def palindrome(num):
    if type(num)!= int or num<0:
        return "Not valid"
    
    if num <10:
        return 11
    
    a = str(num)
    if a == a[::-1]:
        return num
    pos = num+1
    ant =num-1

    
    while True:
        a = str(pos)
        
        b = str(ant)
        
        if a == a[::-1]:
            return pos
        
        if b == b[::-1]:
            return ant
        pos +=1
        ant-=1