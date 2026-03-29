def sudoku(puzzle):
    rows = [set(range(1, 10)) for _ in range(9)]
    cols = [set(range(1, 10)) for _ in range(9)]
    boxes = [set(range(1, 10)) for _ in range(9)]

    # initialize sets
    for r in range(9):
        for c in range(9):
            v = puzzle[r][c]
            if v:
                rows[r].remove(v)
                cols[c].remove(v)
                boxes[(r//3)*3 + c//3].remove(v)

    empties = [(r, c) for r in range(9) for c in range(9) if puzzle[r][c] == 0]

    def backtrack(i=0):
        if i == len(empties):
            return True

        # choose the cell with the fewest candidates (MRV)
        # (makes it faster even for harder puzzles)
        min_i = i
        min_choices = None
        for j in range(i, len(empties)):
            r, c = empties[j]
            choices = rows[r] & cols[c] & boxes[(r//3)*3 + c//3]
            if min_choices is None or len(choices) < len(min_choices):
                min_choices = choices
                min_i = j
                if len(min_choices) == 1:
                    break

        # swap chosen cell into current position
        empties[i], empties[min_i] = empties[min_i], empties[i]
        r, c = empties[i]
        b = (r//3)*3 + c//3
        choices = rows[r] & cols[c] & boxes[b]

        for v in choices:
            puzzle[r][c] = v
            rows[r].remove(v); cols[c].remove(v); boxes[b].remove(v)

            if backtrack(i + 1):
                return True

            rows[r].add(v); cols[c].add(v); boxes[b].add(v)
            puzzle[r][c] = 0

        return False

    backtrack()
    return puzzle
