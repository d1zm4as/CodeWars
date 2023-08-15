def spin_words(s):
    arr = s.split()

    copy = ""

    for x in arr:
        if len(x)>=5:
            copy+= x[::-1]
            copy+= " "
        else:
            copy+=x
            copy+= " "

    return copy.strip()


