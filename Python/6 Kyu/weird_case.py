def to_weird_case(s):
    total = ""
    for x in s.split():
        copy = ""  
        for idx,y in enumerate(x):
            if idx%2==0:
                copy+=y.upper()
            else:
                copy+=y.lower()
        total+=copy
        total+=" "
    return total.rstrip()
