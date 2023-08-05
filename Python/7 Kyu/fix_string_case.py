def solve(s):
    return s.lower() if len([x for x in s if x.islower()]) >= len([x for x in s if x.isupper()]) else s.upper()
