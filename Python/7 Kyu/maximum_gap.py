def max_gap(numbers):
    numbers = sorted(numbers)
    maior = numbers[1] - numbers[0]
    for x,y in zip(numbers,numbers[1:]):
        diff = y-x
        if diff> maior:
            maior = diff
    return maior