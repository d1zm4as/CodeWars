def sortByBinaryOnes (a): 
    return sorted(a, key=lambda k: (-bin(k).count('1'), k))