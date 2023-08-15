def next_bigger(n):
    s = sorted(str(n))
    tam =int("".join(list(reversed(s))))
    ref = n
    while ref<=tam:
        ref+=1
        refl = sorted(str(ref))
        if refl ==s:
            return ref
    return -1
        