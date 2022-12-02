

def validate_pin(pin):
    
    
    if pin.isnumeric() and len(pin)==4:
        return True
    if pin.isnumeric() and len(pin)==6:
        return True
    else:
        return False

