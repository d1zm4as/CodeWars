
string = "abc"
copy = ""

for x in string: 
    if x =="a":copy+="b"
    elif x =="b":copy+="a"
    else:copy+=x


print(copy)