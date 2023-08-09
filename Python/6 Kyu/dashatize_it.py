def impar(x):
    return True if int(x)%2!=0 else False
def dashatize(n):
    ex = str(n)
    copy = ""
    for x in ex:
        if x.isdigit() and impar(x):
            copy+= f"-{x}-"
        else:
            copy+=x

    copy = copy.strip("-")
    copy = copy.replace("--", "-")
    return copy