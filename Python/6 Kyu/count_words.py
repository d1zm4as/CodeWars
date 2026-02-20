import re

_NOP = {"a", "the", "on", "at", "of", "upon", "in", "as"}

def word_count(text):
    """Return number of words (ASCII a-z sequences) excluding stop words.

    Words are contiguous runs of ASCII letters A-Z/a-z. The comparison
    for excluded words is case-insensitive.
    """
    if not text:
        return 0
    words = re.findall(r"[A-Za-z]+", text)
    count = 0
    for w in words:
        if w.lower() not in _NOP:
            count += 1
    return count