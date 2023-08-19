from random import randint


def generate(l):
    copy = ""
    for x in range(l):
        a = randint(0,1)
        copy+=str(a)
    return copy