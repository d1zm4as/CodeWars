# Given an array of 4 integers
# [a,b,c,d] representing two points (a, b) and (c, d), return a string representation of the slope of the line joining these two points.

# For an undefined slope (division by 0), return undefined . Note that the "undefined" is case-sensitive.

def find_slope(points):
    a, b, c, d = points
    if c - a == 0:
        return "undefined"
    return str(int((d - b) / (c - a)))