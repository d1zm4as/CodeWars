from itertools import permutations as perm
def permutations(s):
    # Code Away!
    perms = set([''.join(x) for x in perm(s)])

    return list(perms)
    