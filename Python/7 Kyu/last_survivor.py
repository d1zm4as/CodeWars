def last_survivor(letters, coords):
    for x in coords:
        letters = letters[0:x] + letters[x+1:]
    return letters