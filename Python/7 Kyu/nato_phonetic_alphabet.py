def nato(word):
    copy = ""
    
    for x in word:
        x  = x.upper()
        copy+=LETTERS[x]
        copy+=" "
    return copy.rstrip()