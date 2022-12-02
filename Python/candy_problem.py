def candies(s):
    if len(s)==0 or len(s)==1:
        return -1
    else:
        maior= max(s)
        lista = [x for x in s if x !=maior]
        total= [maior -y for y in lista ]
        return sum(total)
