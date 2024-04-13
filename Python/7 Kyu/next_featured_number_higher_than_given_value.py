def check(a):
    n = str(a)
    if len(n)!=len(set(n)):
        return False
    if a%2==0:
        return False
    if a%3==0:
        return True
    return False


def next_numb(val):
    if val == 9999999999:
        return "There is no possible number that fulfills those requirements"
    val+=1
    while True:
        if check(val):
            return val
        val+=1