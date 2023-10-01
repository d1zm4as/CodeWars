def gimme_the_letters(rng):
    a,b = map(ord, rng.split('-'))
    return ''.join(map(chr, range(a,b+1))) 