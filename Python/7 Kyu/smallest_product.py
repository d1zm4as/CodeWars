from math import prod
def smallest_product(a):
    return min([prod(x) for x in a])