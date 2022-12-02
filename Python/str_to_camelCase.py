def to_camel_case(text):
    #your code herdlfldfde
    s = text.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(text) == 0:
        return text
    return s[0] + ' '.join(s[1:]).title().replace(" ", "")
