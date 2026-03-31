def take_num(s):
    num = ''
    for i in s[::-1]:
        if i.isdigit():
            num = i + num
        else:
            break
    return num

def increment_string(s):
    if not s:
        return "1"
    if not take_num(s):
        return s+"1"
    num = take_num(s)
    tam = len(num)
    incremented_num = str(int(num) + 1).zfill(tam)  
    return s[:-tam] + incremented_num 