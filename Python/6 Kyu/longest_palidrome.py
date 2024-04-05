def longest_palindrome (s):

    maior = 0

    for j in range(1, len(s)+1):
        for i in range(j):
            sub = s[i:j]
            if sub == sub[::-1]:
                maior = max(maior, len(sub))

    return maior