arr = [0, 2, 0, 0, 0, 0, 3, 4, 5, 0, 0, 0, 0, 0]

cont = 0
copy = ""
for x in arr:
    
    if x==0:
       copy+="0"
    else:
        copy+=","


print(copy)
lol = copy.split(",")

print(lol)

lol  = [x for x in lol if x.isdigit()]

print(lol)