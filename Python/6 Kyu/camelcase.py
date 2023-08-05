def camelcase(s):
    b= ''.join(' ' + x if x.isupper() else x for x in s)
    return len(b.split())
