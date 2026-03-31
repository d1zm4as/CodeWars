
def mat_mult(a, b):
    # Multiplies two 3x3 matrices
    res = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                res[i][j] += a[i][k] * b[k][j]
    return res

def mat_pow(mat, power):
    # Fast exponentiation of 3x3 matrix
    result = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
    while power:
        if power % 2:
            result = mat_mult(result, mat)
        mat = mat_mult(mat, mat)
        power //= 2
    return result

def padovan(n):
    if n < 3:
        return 1
    M = [
        [0, 1, 1],
        [1, 0, 0],
        [0, 1, 0],
    ]
    v = [1, 1, 1]
    Mp = mat_pow(M, n-2)
    # Multiply Mp[0] by v
    result = Mp[0][0]*v[0] + Mp[0][1]*v[1] + Mp[0][2]*v[2]
    return result


if __name__ == "__main__":
    # Basic tests
    for i in range(10):
        print(f"padovan({i}) = {padovan(i)}")
    print(f"padovan(1_000_000) = {padovan(1_000_000)}")