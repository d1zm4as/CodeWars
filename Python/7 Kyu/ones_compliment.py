def ones_complement(bi):
    copy = ""
    for x in bi:
        if x == "1":
            copy+="0"
        elif x == "0":
            copy+="1"
    return copy
