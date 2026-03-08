# # There are several difficulty of sudoku games, we can estimate the difficulty of a sudoku game based on how many cells are given of the 81 cells of the game.

#     Easy sudoku generally have over 32 givens
#     Medium sudoku have around 30–32 givens
#     Hard sudoku have around 28–30 givens
#     Very Hard sudoku have less than 28 givens

# Note: The minimum of givens required to create a unique (with no multiple solutions) sudoku game is 17.

# A hard sudoku game means that at start no cell will have a single candidates and thus require guessing and trial and error. A very hard will have several layers of multiple candidates for any empty cell.
# Task:

# Write a function that solves sudoku puzzles of any difficulty. The function will take a sudoku grid and it should return a 9x9 array with the proper answer for the puzzle.

# Or it should raise an error in cases of: invalid grid (not 9x9, cell with values not in the range 1~9); multiple solutions for the same puzzle or the puzzle is unsolvable

# Should as fast as possible, so it should be optimized for performance. The function should be able to solve a hard sudoku game in less than 1 second. More faster is better.

def sudoku_solver(grid):
    # Check if the grid is valid
    if len(grid) != 9 or any(len(row) != 9 for row in grid):
        raise ValueError("Invalid grid: Grid must be 9x9.")
    
    for row in grid:
        for cell in row:
            if cell != 0 and (cell < 1 or cell > 9):
                raise ValueError("Invalid grid: Cell values must be in the range 1-9.")
    
    # Helper function to check if placing a number is valid
    def is_valid(num, pos):
        # Check row
        for i in range(9):
            if grid[pos[0]][i] == num and pos[1] != i:
                return False
        
        # Check column
        for i in range(9):
            if grid[i][pos[1]] == num and pos[0] != i:
                return False
        
        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if grid[i][j] == num and (i, j) != pos:
                    return False
        
        return True
    
    # Backtracking solver function
    def solve():
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:  # Find an empty cell
                    for num in range(1, 10):  # Try numbers 1-9
                        if is_valid(num, (i, j)):
                            grid[i][j] = num
                            
                            if solve():
                                return True
                            
                            grid[i][j] = 0  # Reset the cell (backtrack)
                    
                    return False  # Trigger backtracking
        
        return True  # Puzzle solved
    
    if not solve():
        raise ValueError("The puzzle is unsolvable.")
    
    return grid