def calculate_age(y, c):
    diff  = c-y
    if diff > 0:
        if diff==1:
            return f"You are {diff} year old."            
        else:
            return f"You are {diff} years old."
    if diff < 0:
        if diff== -1:
            return f"You will be born in {diff*-1} year."            
        else:
            return f"You will be born in {diff*-1} years."            
            
    
    if diff == 0:
        return "You were born this very year!"