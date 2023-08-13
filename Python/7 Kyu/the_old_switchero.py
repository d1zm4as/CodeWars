def vowel_2_index(s):
    copy = ""
    for idx, x in enumerate(s,start =1):
        if x in "aeiouAEIOU":
            copy+=str(idx)
        else:
            copy+=x
    return copy