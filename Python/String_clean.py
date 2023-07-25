def string_clean(s):
    """
    Function will return the cleaned string
    """
    copy = ""
    for x in s:
        if not x.isdigit():
            copy+=x
    return copy
