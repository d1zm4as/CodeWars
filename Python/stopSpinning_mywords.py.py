s = "Hey fellow warriors"

arr = s.split()

copy = ""

for x in arr:
    if len(x)>=5:
        copy+= x[::-1]
        copy+= " "
    else:
        copy+=x
        copy+= " "

print(copy.strip())