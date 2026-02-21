

def decipher(code):
    result = ""
    for i in range(len(code[0])):
        sum_ = 0
        for j in range(len(code)):
            char = code[j][i]
            if char == ' ':
                sum_ += 0
            else:
                sum_ += ord(char) - ord('a') + 1
        avg = sum_ // len(code)
        if avg == 0:
            result += ' '
        else:
            result += chr(avg + ord('a') - 1)
    return result