
from collections import Counter

def find_characters(matrix):

    conta = Counter(matrix.replace('\n', ''))
    min_count = min(conta.values())
    return ''.join(sorted([k for k, v in conta.items() if v == min_count], key=lambda x: (x.isdigit(), x.isalpha(), x.islower(), x)))