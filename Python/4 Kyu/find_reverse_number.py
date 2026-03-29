# Reverse Number is a number which is the same when reversed.

# For example, the first 20 Reverse Numbers are:

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101

# TASK:

#     You need to return the nth reverse number. (Assume that reverse numbers start from 0 as shown in the example.)

# NOTES:
# """ Return the nth number in sequence of reversible numbers.

#     For reversible numbers, a pattern emerges when compared to n:
#     if we subtract a number made of a sequence of the digit 9
#     (i.e. 9, 99, 999, our magic number) from n, the result forms 
#     the left half of the nth reversible number starting from 0.
#     The number of digits "9" in the magic number increases every
#     time n reaches an order of magnitude of the number 11; the
#     width of that order of magnitude is the width of the magic number.
#     That width also tells us how many digits of the left half must
#     be mirrored to form the final, nth reversible number.
    
#     Examples (_ digits get mirrored, | digits remain static)
    
#         n = 109    ->   100  ->  1001
#                    -9   _||      _||_
        
#         n = 110    ->   11   ->  1111
#                   -99   __       ____
                  
#         n = 1099   ->  1000  ->  100001
#                   -99  __||      __||__
                  
#         n = 1100   ->  101   ->  101101
#                  -999  ___       ______


def find_reverse_number(n: int) -> int:
    

    k = n - 1  # zero-based index in the palindrome sequence

    # length 1 palindromes: 0..9 (10 numbers)
    if k < 10:
        return k

    k -= 10  # skip 1-digit palindromes

    length = 2
    while True:
        half_len = (length + 1) // 2
        count = 9 * (10 ** (half_len - 1))  # palindromes of this length

        if k < count:
            start = 10 ** (half_len - 1)
            half = start + k
            s = str(half)
            if length % 2 == 0:
                return int(s + s[::-1])
            else:
                return int(s + s[-2::-1])  # mirror without duplicating middle digit
        else:
            k -= count
            length += 1
