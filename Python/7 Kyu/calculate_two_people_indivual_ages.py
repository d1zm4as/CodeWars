def get_ages(sum_, difference):
    if sum_<0 or difference <0:
        return None
    b = (sum_ - difference)/2
    if b<0:
        return None
    a = sum_-b
    return (a,b)