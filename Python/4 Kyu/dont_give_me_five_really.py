# Your mission, should you accept it, is to return the count of all integers in a given range which do not contain the digit 5 (in base 10 representation).
# You are given the start and the end of the integer range. The start and the end are both inclusive.

# Examples:

# 1,9 -> 1,2,3,4,6,7,8,9 -> return 8
# 4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> return 12

# The result may contain fives. ;-)
# The start will always be smaller than the end. Both numbers can be also negative.

# The regions can be very large and there will be a large number of test cases. So brute force solutions will certainly time out!

# Good luck, warrior!, remember it has to work for very large regions, so think about performance!
#        test.assert_equals(dont_give_me_five(0, 1), 2)
#         test.assert_equals(dont_give_me_five(5, 15), 9)
#         test.assert_equals(dont_give_me_five(-5, 4), 9)
#         test.assert_equals(dont_give_me_five(51, 60), 1)
#     test.assert_equals(dont_give_me_five(40076, 2151514229639903569), 326131553237897713)
# #         test.assert_equals(dont_give_me_five(-206981731, 2235756979031654521), 340132150309630357)
# #         test.assert_equals(dont_give_me_five(-2490228783604515625, -2490228782196537011), 520812180)    
# #         test.assert_equals(dont_give_me_five(-9000000000000000000, 9000000000000000000), 2401514164751985937)
# test.assert_equals(dont_give_me_five(984, 4304), 2449)
# #         test.assert_equals(dont_give_me_five(2313, 2317), 4)
# #         test.assert_equals(dont_give_me_five(-4045, 2575), 4819)
# #         test.assert_equals(dont_give_me_five(-4436, -1429), 2194)
# test.assert_equals(dont_give_me_five(-17, 9), 24)
#         test.assert_equals(dont_give_me_five(1, 9), 8)
#         test.assert_equals(dont_give_me_five(4, 17), 12)
#         test.assert_equals(dont_give_me_five(-17, -4), 12)
def _count_no5_upto(n):
    if n < 0:
        return 0
    s = str(n)
    L = len(s)
    # numbers with fewer digits
    res = 0
    for k in range(1, L):
        if k == 1:
            res += 9
        else:
            res += 8 * (9 ** (k - 1))
    # count same-length numbers <= n
    for i, ch in enumerate(s):
        d = ord(ch) - 48
        rem = L - i - 1
        if i == 0:
            # first digit: choices 1..d-1 excluding 5
            smaller = sum(1 for x in range(1, d) if x != 5)
        else:
            # other digits: choices 0..d-1 excluding 5
            smaller = sum(1 for x in range(0, d) if x != 5)
        res += smaller * (9 ** rem)
        if d == 5:
            return res
    return res + 1


def dont_give_me_five(come_from, come_to):
    a, b = come_from, come_to
    if a > b:
        a, b = b, a
    if a >= 0:
        lo = _count_no5_upto(a - 1) if a else 0
        return _count_no5_upto(b) - lo
    if b < 0:
        return _count_no5_upto(-a) - _count_no5_upto(-b - 1)
    # a < 0 <= b
    return _count_no5_upto(-a) + _count_no5_upto(b) - 1