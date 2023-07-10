#n = 274
# n = 6815
#n = 86320
#n = 5311
#n = 974302
ex = str(n)
copy = ""

def impar(x):
    return True if int(x)%2!=0 else False

for x in ex:
    if x.isdigit() and impar(x):
        copy+= f"-{x}-"
    else:
        copy+=x

copy = copy.strip("-")
copy = copy.replace("--", "-")
print(copy)