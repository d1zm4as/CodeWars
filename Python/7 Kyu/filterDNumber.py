def filter_string(string):
    a = "".join([x for x in string if x.isdigit()])
    
    return int(a) 

