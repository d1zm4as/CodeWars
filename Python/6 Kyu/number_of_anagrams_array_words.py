from collections import Counter
def anagram_counter(words):
    """Return the total number of distinct pairs of anagramic words in the array."""
    count = Counter(tuple(sorted(w)) for w in words)
    return sum(c * (c - 1) // 2 for c in count.values())