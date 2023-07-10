# def create_phone_number(n):
    # arr = [str(x) for x in n]
    # copy = ""
    # copy+="("
    # pri = "".join(arr[:3])
    # copy+=pri+")"+" "
    
    # mid = "".join(arr[3:6])
    # copy+=mid+"-"
    # fim = "".join(arr[6:])
    # copy+=fim
	# return "({}{}{}) {}{}{}-{}{}{}{}".format(n)


def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
n = [0,1,2,3,4,5,6,7,8,9]
print(create_phone_number(n))