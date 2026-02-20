def solve(s):
    if len(s) % 2 != 0:
        return -1

    stack = []
    reversals = 0

    for char in s:
        if char == '(':
            stack.append(char)
        else:  # char == ')'
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                reversals += 1
                stack.append('(')  # Treat this as an opening parenthesis for future matches

    # The remaining items in the stack are unmatched opening parentheses
    reversals += len(stack) // 2

    return reversals