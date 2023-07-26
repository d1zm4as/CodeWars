

a = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]


def open_or_senior(a):
    return ["Senior" if x[0]>=55 and x[1]>7 else "Open" for x in a ]


a = {"a":1}
b = {"b":2}


print(a|b)