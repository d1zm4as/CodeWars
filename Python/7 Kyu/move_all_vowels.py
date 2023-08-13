def move_vowels(input): 
    vowels = ""
    copy = ""
    for x in input:
        if x not in "aeiou":
            copy+=x
        else:
            vowels+=x
    copy+=vowels
    return copy