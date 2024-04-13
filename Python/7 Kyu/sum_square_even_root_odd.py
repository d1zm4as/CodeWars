def sum_square_even_root_odd(nums):
    lista= [ ]
    for x in nums:
        if x%2==0:
            lista.append(x**2)
        else:
            lista.append(x**.5)
    return round(sum(lista),2)
            
