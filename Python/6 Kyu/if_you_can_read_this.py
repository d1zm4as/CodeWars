from preloaded import NATO

def to_nato(words):
    return ' '.join(NATO.get(c.upper(), c) for c in words if c != ' ')