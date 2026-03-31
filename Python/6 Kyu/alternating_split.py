# Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

# Examples:

# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"

# Together with the encryption function, you should also implement a decryption function which reverses the process.

# If the string S is an empty value or the integer N is not positive, return the first argument without changes.

def decrypt(encrypted_text, n):
    copy = ""
    if encrypted_text == "" or n <= 0:
        return encrypted_text
    for i in range(len(encrypted_text) // 2):
        copy += encrypted_text[len(encrypted_text) // 2 + i]
        copy += encrypted_text[i]
    if len(encrypted_text) % 2 != 0:    
        copy += encrypted_text[len(encrypted_text) - 1]
    return decrypt(copy, n - 1) 


def encrypt(text, n):
    copy = ""
    if text == "" or n <= 0:
        return text
    for i in range(1, len(text), 2):
        copy += text[i]
    for i in range(0, len(text), 2):
        copy += text[i]
    return encrypt(copy, n - 1)