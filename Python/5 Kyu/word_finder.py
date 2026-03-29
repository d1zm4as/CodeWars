# In this kata you have to extend the dictionary with a method, that returns a list of words matching a pattern. This pattern may contain letters (lowercase) and placeholders ("?"). A placeholder stands for exactly one arbitrary letter.

# Example:
class Dictionary:
    def __init__(self, words):
        self.words = words

    def get_matching_words(self,pattern):
        return [word for word in self.words if len(word) == len(pattern) and all(p == w or p == '?' for p, w in zip(pattern, word))]