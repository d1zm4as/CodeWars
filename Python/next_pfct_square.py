

def find_next_square(sq):
    a  = sq**0.5
    if a.is_integer()==True:
        return  (a+1)**2 
    else: 
        return -1
    

