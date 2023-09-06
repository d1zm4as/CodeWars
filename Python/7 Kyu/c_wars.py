def initials(name):
    s = name.split()
    ul = s[-1].title()
    copy = ""
    for x in s[:-1]:
        copy+=x[0].title()
        copy+="."
    copy+=ul
    return copy