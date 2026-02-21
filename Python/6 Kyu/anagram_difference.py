from statistics import Counter
def anagram_difference(w1, w2):
    """Return the number of letters that must be removed from the two words to make them anagrams."""

    c1, c2 = Counter(w1), Counter(w2)
    return sum((c1 - c2).values()) + sum((c2 - c1).values())