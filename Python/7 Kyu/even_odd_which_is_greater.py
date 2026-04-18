def Odd(s):
    return int(s) & 1


def even_or_odd(s):
    # your code here
    sum_odd = 0
    sum_even = 0

    for x in s:
        if Odd(x):
            sum_odd += int(x)
        else:
            sum_even += int(x)

    if sum_odd > sum_even:
        return "Odd is greater than Even"
    if sum_even > sum_odd:
        return "Even is greater than Odd"
    return "Even and Odd are the same"
