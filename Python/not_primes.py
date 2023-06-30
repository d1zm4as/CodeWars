from gmpy2 import is_prime



def check(n):
    for x in str(n):
        if x not in "2357":
            return False
    return True


a,b = 2,222




print([x for x in range(a,b) if not  is_prime(x) and check(x)])

