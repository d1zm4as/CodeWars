
def vowel_recognition(s):
    vowels = set('aeiouAEIOU')
    count = 0
    for i, char in enumerate(s):
        if char in vowels:
            count += (i + 1) * (len(s) - i)
    return count