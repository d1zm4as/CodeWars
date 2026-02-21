def consecutive_nums(lst, group_len):
    if len(lst) % group_len != 0:
        return False
    from collections import Counter
    count = Counter(lst)
    nums = sorted(count)
    while count:
        first = min(count)
        for i in range(group_len):
            num = first + i
            if count.get(num, 0) == 0:
                return False
            count[num] -= 1
            if count[num] == 0:
                del count[num]
    return True