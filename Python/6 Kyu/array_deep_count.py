def deep_count(a):
    result = 0
    for i in range(len(a)):
        if type(a[i]) is list:
            result += deep_count(a[i])
        result += 1
    return result
           



# lista = [1, 2, [3, 4, [5]]] 
lista = [[[[[[[[[]]]]]]]]]