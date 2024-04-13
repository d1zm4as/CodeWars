def pali(s):
    return s==s[::-1]


s = "A"
s = "Hannah"
s = "xyz__a_/b0110//a_zyx"
def longest_palindrome (s):

    maior = 0

    copy = ""

    for x in s.lower():
        copy+=x
        if pali(copy):
            maior = max(len(copy),maior)
        
    return maior

print(longest_palindrome(s))