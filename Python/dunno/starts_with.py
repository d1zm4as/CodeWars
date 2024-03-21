def solution(string, ending):
    """
    a = string[len(string)-len(ending):]
    #print(a)
    #print(ending)
    if a == ending:
        return True
    return False
    """
    return True if string[len(string)-len(ending):]==ending else False
