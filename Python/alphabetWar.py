def alphabet_war(fight):
    if len(fight)==1:return "Right side wins!"
    e = { 'd': 4, 'm': 4,  'q': 3,'z':1}

    r= {'b': 2,'p': 3,'s': 1,'w': 4}
    some = 0
    somr = 0
    for x in fight:
        if x in e:
            some+=e[x]
        elif x in r:
            somr+=r[x]
    if somr>some:
        return "Rigth side wins!"
    if some>somr:
        return "Left side wins!"
    return "Let's fight again!"