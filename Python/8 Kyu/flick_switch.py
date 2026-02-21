def flick_switch(lst):
    result = []
    current_value = True  # Start with True
    for item in lst:
        if item == 'flick':
            current_value = not current_value  # Switch the value
        result.append(current_value)
    return result