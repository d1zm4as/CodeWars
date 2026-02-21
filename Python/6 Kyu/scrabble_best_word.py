
def get_best_word(points, words):
    best_score = 0
    best_index = 0
    for i, word in enumerate(words):
        score = sum(points[ord(c) - ord('A')] for c in word)
        if score > best_score or (score == best_score and len(word) < len(words[best_index])):
            best_score = score
            best_index = i
    return best_index