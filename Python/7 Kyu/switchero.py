def switcheroo(string):
    copy = ""

    for x in string: 
        if x =="a":copy+="b"
        elif x =="b":copy+="a"
        else:copy+=x

    return copy