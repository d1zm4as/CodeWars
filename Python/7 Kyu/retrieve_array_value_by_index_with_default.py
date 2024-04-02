def solution(items, index, default_value):
    if abs(index)>len(items):
        return default_value
    return items[index]