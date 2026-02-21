
def valid_phone_number(phone_number):
    if len(phone_number) != 14:
        return False
    if phone_number[0] != '(' or phone_number[4] != ')' or phone_number[5] != ' ' or phone_number[9] != '-':
        return False
    for i in [1, 2, 3, 6, 7, 8, 10, 11, 12, 13]:
        if not phone_number[i].isdigit():
            return False
    return True