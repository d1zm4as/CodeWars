from gmpy2 import is_odd

def is_odd_heavy(arr):
    par = [x for x in arr if not is_odd(x)]
    imp = [x for x in arr if is_odd(x)]
    return len(imp) > 0 and all(i > p for i in imp for p in par)