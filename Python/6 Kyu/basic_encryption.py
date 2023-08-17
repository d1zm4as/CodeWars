def encrypt(text, rule):
    copy = ""
    
    
    for x in text:
        item = chr((ord(x)+rule)%256)
        copy+=item
    return copy