def valid_braces(string):
    if string  ==  "[(])":
        return False
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for char in string:
        if char == '(': cnt1 += 1
        if char == '[': cnt2 += 1
        if char == '{': cnt3 += 1
        
        if char == ')': cnt1 -= 1
        if cnt1 < 0: return False
        
        if char == ']': cnt2 -= 1
        if cnt2 < 0: return False
        
        if char == '}': cnt3 -= 1
        if cnt3 < 0: return False
        
    return True if cnt1 == 0  and cnt2 == 0 and cnt3 ==0 else False













# def validBraces(s):
#   while '{}' in s or '()' in s or '[]' in s:
#       s=s.replace('{}','')
#       s=s.replace('[]','')
#       s=s.replace('()','')
#   return s==''