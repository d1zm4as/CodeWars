def remove_parentheses(s):
    copy = ""

    cont = 0
    for x in s:
        if x != "(" and cont == 0:
            copy+=x
        elif x == "(":
            cont+=1
        elif x==")":
            cont-=1
    return copy