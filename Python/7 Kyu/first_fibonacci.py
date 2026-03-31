def solution(f, s):
    while s - f >= 0:
        f, s = s - f, f
    return (s, f + s)