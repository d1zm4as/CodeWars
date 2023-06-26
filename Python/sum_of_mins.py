def sum_of_minimums(numbers):
    soma = 0
    for x in numbers:
        soma+=min(x)
    return soma