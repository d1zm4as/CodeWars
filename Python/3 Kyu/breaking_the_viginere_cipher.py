def get_keyword(ciphertext, key_len):
    # English letter frequencies (A..Z)
    EN_FREQ = [
        0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
        0.00978, 0.02360, 0.00150, 0.01974, 0.00074
    ]

    A = ord('A')
    # count ciphertext letters per key position
    cols = [[0]*26 for _ in range(key_len)]
    for i, ch in enumerate(ciphertext):
        cols[i % key_len][ord(ch) - A] += 1

    key = []
    for counts in cols:
        n = sum(counts)
        if n == 0:
            key.append('A')
            continue
        exp = [f * n for f in EN_FREQ]

        best_shift = 0
        best_score = float('inf')

        for s in range(26):
            # decrypted letter j corresponds to ciphertext letter (j + s) % 26
            chi = 0.0
            for j in range(26):
                obs = counts[(j + s) % 26]
                e = exp[j]
                diff = obs - e
                chi += diff * diff / e
            if chi < best_score:
                best_score = chi
                best_shift = s

        key.append(chr(A + best_shift))

    return ''.join(key)
