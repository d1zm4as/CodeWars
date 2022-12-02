

def disemvowel(string_):
    
    mod= [x for x in string_ if x not in "aeiouAEIOU"]
    
    x = "".join(mod)
    return x


