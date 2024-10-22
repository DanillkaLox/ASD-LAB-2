def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1 or \
           (col - (row - i) >= 0 and board[i][col - (row - i)] == 1) or \
           (col + (row - i) < 8 and board[i][col + (row - i)] == 1):
            return False
    return True

def ldfs(board, row, max_depth):
    if row >= max_depth:
        return True

    for col in range(8):
        if is_safe(board, row, col):
            board[row][col] = 1
            if ldfs(board, row + 1, max_depth):
                return True
            board[row][col] = 0

    return False

def solve_n_queens(max_depth=8):
    board = [[0 for _ in range(8)] for _ in range(8)]
    if ldfs(board, 0, max_depth):
        for row in board:
            print(row)
    else:
        print("No solution")

solve_n_queens()