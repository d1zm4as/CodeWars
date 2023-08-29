def special_number(number):
    check  = {0,1,2,3,4,5}
    for x in str(number):
        if int(x) not in check:
            return "NOT!!"
    return "Special!!"