def digit_multiplication(s):
    total = 0
    current_product = 1
    current_sign = 1

    for char in s:
        if char.isdigit():
            current_product *= int(char)
        else:
            total += current_sign * current_product
            current_product = 1
            current_sign = 1 if char == '+' else -1

    total += current_sign * current_product
    return total