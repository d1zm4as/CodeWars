def get_number_from_string(string):
    return  int("".join([x for x in string if x.isdigit()]))