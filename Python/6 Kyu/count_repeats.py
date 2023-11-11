def count_repeats(s):
    copy = s[0]
    atual = s[0]
    for x in s[1:]:
        print(x)
        if x!= atual:
            copy+=x
            atual = x
        else:
            atual = x
    return len(s)-len(copy)