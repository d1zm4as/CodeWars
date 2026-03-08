
def remove_consecutive_duplicates(s):
    result = []
    for char in s:
        if not result or char != result[-1]:
            result.append(char)
    return ''.join(result)

def dup(s):
    return [remove_consecutive_duplicates(x) for x in s]