def small_enough(array, limit):
    for x in array:
        if x > limit:
            return False
    return True
