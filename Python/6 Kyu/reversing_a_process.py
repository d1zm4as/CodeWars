
def decode(r):
    num = int(''.join(filter(str.isdigit, r)))
    r = ''.join(filter(str.isalpha, r))
    s = ''
    try:
        for ch in r:
            x = (ord(ch) - ord('a')) * pow(num, -1, 26) % 26
            s += chr(x + ord('a'))
        return s
    except ValueError:
        return "Impossible to decode"