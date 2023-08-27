from bisect import bisect_left

def keep_order(ary, val):
    # your code here
    return bisect_left(ary,val)