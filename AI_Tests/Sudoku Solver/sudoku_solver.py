def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def is_valid(board, num, position):
    # Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][position[1]] == num and position[0] != i:
            return False

    # Check 3x3 grid
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != position:
                return False

    return True

def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True
    else:
        row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

# Example Sudoku board
board = [
    [0, 0, 0, 0, 6, 9, 0, 0, 0],
    [7, 2, 0, 0, 3, 0, 6, 0, 0],
    [0, 0, 6, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 8, 7],
    [0, 0, 0, 8, 9, 5, 2, 0, 1],
    [0, 0, 2, 1, 7, 0, 4, 0, 0],
    [6, 8, 3, 0, 1, 4, 7, 0, 2],
    [0, 4, 0, 0, 0, 0, 1, 0, 6],
    [2, 1, 0, 0, 0, 0, 0, 0, 0]
]

print("Sudoku puzzle to solve:")
print_board(board)
print("\nSolving...\n")

if solve_sudoku(board):
    print("Sudoku puzzle solved successfully!")
    print("\nSolved Sudoku:")
    print_board(board)
else:
    print("No solution exists for this Sudoku puzzle.")
