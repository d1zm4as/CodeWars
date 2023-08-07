def zero_plentiful(arr) :
    if len(arr) <3:return 0
    cont = 0
    copy = ""
    for x in arr:

        if x==0:
            copy+="0"
        else:
            copy+=","


    lol = copy.split(",")


    lol  = [x for x in lol if x.isdigit()]
    cont = 0
    for x in lol :
        if len(x)<4:
            return 0
        else:
            cont+=1
    return cont
    
