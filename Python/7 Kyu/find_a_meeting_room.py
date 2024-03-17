def meeting(rooms):
    for x in range(0,len(rooms)):
        if rooms[x]=="O":
            return x
    return "None available!"
    
    
