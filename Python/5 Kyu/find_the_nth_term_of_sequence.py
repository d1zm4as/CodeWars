# given the first few terms of a sequence, can you figure out the formula that was used to generate these numbers, so we can find any term in the sequence?
# Task

#     write a function that accepts an array of number(the first few terms of a sequence)
#     your function should return a mapping function that accepts an integer(n) and then return the nth term of the sequence, where zero is the first term.
#     in practice a sequance can be completed in many ways, assume that the equation used is a Polynomial, and find the simplest(smallest degree) equation possible, that leaves you with a single unique solution.

# Examples
# input 	equation 	degree 	more terms
# [2, 4, 6] 	2x+2 2x+2 2x+2 	1 1 1 	2, 4, 6, 8, 10, 12, ...
# [100, 101] 	x+100 x+100 x+100 	1 1 1 	100, 101, 102, 103, ...
# [5] 	5 5 5 	0 0 0 	5, 5, 5, 5, 5, 5, ...
# [6, 17, 88, 321, 866] 	2x4+5x3+x2+3x+6 2x^4+5x^3+x^2+3x+6 2x4+5x3+x2+3x+6 	4 4 4 	6, 17, 88, 321, 866, 1921, ...
# [1, 1, 1, 7] 	x3−3x2+2x+1 x^3-3x^2+2x+1 x3−3x2+2x+1 	3 3 3 	1, 1, 1, 7, 25, 61, ...
# [] 	0 0 0 	0 0 0 	0, 0, 0, 0, 0, 0, ...
# [3, 2, 1] 	−x+3 -x+3 −x+3 	1 1 1 	3, 2, 1, 0, -1, -2, ...
# Notes

#     your solution should support at least equations of degree 0 to 9
#     your solution should run fast when n is big
#     all tests are random, but you don't need to worry about invalid input
#     always return a solution even if you get empty input
#     usually you get more terms than you need, but sometimes you get exactly what you need
#     all sequences have integer terms and uses equations with integer coefficients

# For python, numpy is disabled.

def solve_sequnce(seq):
    def solution(n):
        if not seq:
            return 0
        if len(seq) == 1:
            return seq[0]
        diffs = [seq]
        while len(diffs[-1]) > 1:
            diffs.append([diffs[-1][i+1] - diffs[-1][i] for i in range(len(diffs[-1]) - 1)])
        coeffs = [diff[0] for diff in diffs]
        result = 0
        factorial = 1
        for i in range(len(coeffs)):
            if i > 0:
                factorial *= i
            term = coeffs[i]
            for j in range(i):
                term *= (n - j)
            result += term // factorial
        return result
    return solution