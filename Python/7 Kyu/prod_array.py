def product_array(numbers):
    total = 1
    
    for x in numbers:
        total *= x
    
    return [total // x for x in numbers]