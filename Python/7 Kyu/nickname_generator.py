
def nickname_generator(name):
    if len(name) < 4:
        return "Error: Name too short"
    if name[2] in "aeiou":
        return name[:4]
    return name[:3]