def swap(s, idx1, idx2):
    copy = list(s)
    copy[idx1], copy [idx2] = s [idx2], s[idx1]
    copy = sorted(copy[:idx1]) + copy[idx1:]
    return ''.join(copy)
def next_smaller(n):
    number=str(n)
    if list(number) == sorted(number):
        return -1
    rev_num = number[::-1]
    for i, digit in enumerate(rev_num,0):
        if any(num for num in rev_num[:i] if num < digit):
            _, j = max(((num, j) for j, num in enumerate(rev_num[:i]) if int(num) < int(digit)),key = lambda x:(x[0], x[1]))
            swapped_num = swap(rev_num, i, j)
            if not swapped_num.endswith('0'):
                return int(swapped_num[::-1])
    return -1