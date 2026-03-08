def cont(s):
    if not s:
        return 0
    v  = set('aeiouAEIOU')
    c = 0
    maior = 0 
    for x in s:
        if x in v:
            c += 1
        else:
            maior = max(c, maior)
            c = 0
    return max(c, maior)    

def sort_strings_by_vowels(lst):
    return sorted(lst, key=cont(x), reverse=True)

