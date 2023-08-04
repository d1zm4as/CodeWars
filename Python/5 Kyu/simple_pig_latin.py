def pig_it(s):
    arr =  s.split()

    copy = ""

    for x in arr:
        if x in "!?^~´´":
            copy+=x
            continue
        pri = x[0]
        res = x[1:]
        pes = f"{res}{pri}ay"
        copy+=pes
        copy+=" "
    return copy.strip()

