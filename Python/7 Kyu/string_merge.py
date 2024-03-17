def string_merge(string1, string2,l):
    a = string1.index(l)
    b = string2.index(l)
    copy = string1[:a]+string2[b:]
    return copy