def remove_vowels(strng):
    copy = ""
    v = set("aeiou")
    
    for x in strng:
        if x not in v:
            copy+=x
    return copy