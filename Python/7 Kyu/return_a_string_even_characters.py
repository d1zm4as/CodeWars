def even_chars(s):
    # your code here
    if len(s) < 2 or len(s) > 100:
        return "invalid string"

    return [x for x in s[1::2]]
