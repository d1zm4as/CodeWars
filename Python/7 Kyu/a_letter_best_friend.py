def best_friend(s, a,b):
    if s[-1] == a:
        return False
    for i in range(len(s)-1):
        if s[i] == a and s[i+1] != b:
            return False
    return True

# return t.count(a)==t.count(a+b)