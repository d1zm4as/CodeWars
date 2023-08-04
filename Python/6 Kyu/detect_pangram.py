

def is_pangram(s):
    tira = s.lower()
    a = "qwertyuiopasdfghjklzxcvbnm"
    
    for x in a:
        if x not in tira:
            return False
    return True
    
    

