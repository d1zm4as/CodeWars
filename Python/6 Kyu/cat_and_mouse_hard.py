

def cat_mouse(s,j):
    cat = s.find('C')
    dog = s.find('D')
    mouse = s.find('m')
    if cat == -1 or dog == -1 or mouse == -1:
        return 'boring without all three'
    if abs(cat - mouse) > j:
        return 'Escaped!'
    if (cat < dog < mouse) or (mouse < dog < cat):
        return 'Protected!'
    return 'Caught!'