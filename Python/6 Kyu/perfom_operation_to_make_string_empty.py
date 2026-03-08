from collections import Counter

def last_non_empty_string(s: str) -> str:
    x = Counter(s)
    l = max(x.values()) - 1
    for w in x:
        s = s.replace(w, '', l)
    return s