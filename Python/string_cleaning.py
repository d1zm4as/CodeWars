def string_clean(s):
    """
    Function will return the cleaned string
    """
    return "".join([x for x in s if x not in "0987654321"])
