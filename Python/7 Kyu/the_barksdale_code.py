def decode(s):
    memo = {"1":"9","9":"1","2":"8","8":"2","7":"3","3":"7","4":"6","6":"4","5":"0","0":"5"}
    copy = ""
    for x in s:
        copy+=memo[x]
    return copy
        