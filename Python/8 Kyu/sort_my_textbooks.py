
def sorter(textbooks):
    """Sort a list of textbook titles case-insensitively."""
    return sorted(textbooks, key=str.lower)