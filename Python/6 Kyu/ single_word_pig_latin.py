def pig_latin(s):
    if not s:
        return None
    if not s.isalpha():
        return None
    s = s.lower()
    idx = 0
    termo = ""
    if s[idx] in "aeiou":
        return s+"way"
    con = ""
    
    for x in s:
        if x not in "aeiou":
            con+=x
        else:
            break
        idx+=1
    a = s[idx:]
    lol = a+con+"ay"
    return lol