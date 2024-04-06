def is_safe(board, row, col, n):
    # check if the queen is on the same column
    for i in range(col):
        if (board[row][i] == 1):
            return False
    
    # check if the queen is in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if (board[i][j] == 1):
            return False
        
    # check if the queen is in the upper right diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if (board[i][j] == 1):
            return False
        
    return True


def solve_n_queens_utlity(board, col, n):
    if (col >= n):
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens_utlity(board, (col + 1), n):
                return True
            board[i][col] = 0
            
    return False


def n_queens_solver(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_n_queens_utlity(board, 0, n):
        print("No solution for this one")
        return False
    
    print("Solution for {}-queens problem".format(n))
    for i in range(n):
        for j in range(n):
            print (board[i][j], end=" ")
        print()
        
    return True

grid_num = int(input("Enter the n by n of the board: "))
n_queens_solver(grid_num)

