def par(n):
    return n % 2 == 0

def impar(n):
    return n % 2 != 0


# Given a string of digits, find the longest substring of alternating even and odd digits. Return the substring. 
def longest_substring(digits):
    if not digits:
        return ""
    lista = []
    copy = ""
    for i in range(len(digits)-1):
        if par(int(digits[i])) and impar(int(digits[i+1])):
            copy += digits[i]
        elif impar(int(digits[i])) and par(int(digits[i+1])):
            copy += digits[i]
        else:
            copy += digits[i]
            lista.append(copy)
            copy = ""
    copy += digits[-1]
    lista.append(copy)
    return max(lista, key=len)