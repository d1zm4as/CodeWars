def alphanumeric(password):
    if not password:
        return False
    for x in password:
        if not x.isalpha() and not x.isdigit():
            return False
    return True