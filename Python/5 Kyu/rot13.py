
def rot13(message):
    copy = ""
    for x in message:
        if not x.isalpha():
            copy += x
        elif x.isupper():
            copy += chr((ord(x) - ord('A') + 13) % 26 + ord('A'))
        else:
            copy += chr((ord(x) - ord('a') + 13) % 26 + ord('a'))
    return copy
