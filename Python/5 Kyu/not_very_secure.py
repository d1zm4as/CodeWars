def alphanumeric(password):
    if not password:
        return False
    return password.isalnum()