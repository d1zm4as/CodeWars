
def balanced_num(number):
    num = str(number)
    if len(num) % 2 == 0:
        left = num[:len(num) // 2 - 1]
        right = num[len(num) // 2 + 1:]
    else:
        left = num[:len(num) // 2]
        right = num[len(num) // 2 + 1:]
    if sum(map(int, left)) == sum(map(int, right)):
        return "Balanced"
    else:
        return "Not Balanced"