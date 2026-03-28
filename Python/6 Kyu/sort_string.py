
def sort_string(s):
    letters = sorted([c for c in s if c.isalpha()], key=lambda x: x.lower())
    sorted_letters = []
    for c in s:
        if c.isalpha():
            sorted_letters.append(letters.pop(0))
        else:
            sorted_letters.append(c)
    return ''.join(sorted_letters)