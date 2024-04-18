import copy


grid = [[' ' for _ in range(3)] for _ in range(3)]


def print_layout(grid):
    for row in grid:
        print('|'.join(row))
        print('-' * 5)
def game_over(grid):
    # check the rows, columns and diagonals for the win
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != ' ':
            return True
        if grid[0][i] == grid[1][i] == grid[2][i] != ' ':
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] != ' ':
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] != ' ':
        return True
    
    # check for a tie
    if all (grid[i][j] != ' ' for i in range(3) for j in range(3)):
        return True
    return False


# function to evaluate the game grid
def evaluate_check(grid):
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2]:
            if grid[i][0] == 'X':
                return 1
            elif grid[i][0] == 'O':
                return -1
        if grid[0][i] == grid[1][i] == grid[2][i]:
            if grid[0][i] == 'X':
                return 1
            elif grid[0][i] == 'O':
                return -1
    if grid[0][0] == grid[1][1] == grid[2][2]:
        if grid[0][0] == 'X':
            return 1
        elif grid[0][0] == 'O':
            return -1
    if grid[0][2] == grid[1][1] == grid[2][0]:
            if grid[0][2] == 'X':
                return 1
            elif grid[0][2] == 'O':
                return -1
            
    # no winner in this case 
    return 0

def minmax(grid, depth, is_maximizing):
    if game_over(grid) or depth == 0:
        return evaluate_check(grid)
    if is_maximizing:
        max_evaluation = float('-inf')
        for i in range(3):
            for j in range(3):
                if grid[i][j] == ' ':
                    grid[i][j] = 'X'
                    evaluate = minmax(grid, (depth - 1), False)
                    grid[i][j] = ' '        #revert the move
                    max_evaluation = max(max_evaluation, evaluate)
        return max_evaluation
    else:
        min_evaluation = float('inf')
        for i in range(3):
            for j in range(3):
                if grid[i][j] == ' ':
                    grid[i][j] = 'O'
                    evaluate = minmax(grid, (depth - 1), True)
                    grid[i][j] = ' '        #revert the move
                    min_evaluation = min(min_evaluation, evaluate)
        return min_evaluation
    
def find_best_move(grid):
    best_evaluation = float('-inf')
    best_move = (0, 0)
    for i in range(3):
        for j in range(3):
            if grid[i][j] == ' ':
                grid[i][j] = 'X'
                evaluate = minmax(grid, 3, False)
                grid[i][j] = ' '           #revert the move
                if evaluate > best_evaluation:
                    best_evaluation = evaluate
                    best_move = (i, j)
    return best_move

while not game_over(grid):
    print_layout(grid)
    player_row = int(input("Enter row (0 - 2): "))
    player_col = int(input("Enter columns (0 - 2): "))
    if grid[player_row][player_col] == ' ':
        grid[player_row][player_col] = 'O'
    else:
        print("Invalid move!")
        continue
    
    if game_over(grid):
        break
                    
    comp_row, comp_col = find_best_move(grid)
    print(f"COMP plays at Row:{comp_row} Column:{comp_col}")
    grid[comp_row][comp_col] = 'X'
    
print_layout(grid)
winner = evaluate_check(grid)
if winner == 1:
    print("You Lose!")
elif winner == -1:
    print("You Win!")
else:
    print("Seems like you read minds!")