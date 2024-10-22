import math

reference_solution = [0, 4, 7, 5, 2, 6, 1, 3]

def f3(board):
    misplaced = 0
    for row in range(8):
        for col in range(8):
            if board[row][col] == 1 and reference_solution[row] != col:
                misplaced += 1
    return misplaced

def rbfs(board, row, max_depth, f_limit):
    if row == max_depth:
        return board, 0

    successors = []
    for col in range(8):
        if is_safe(board, row, col):
            new_board = [r[:] for r in board]
            new_board[row][col] = 1
            cost = f3(new_board)
            successors.append([new_board, cost])

    if not successors:
        return None, math.inf

    successors.sort(key=lambda x: x[1])

    best = successors[0]
    alternative = successors[1][1] if len(successors) > 1 else math.inf

    while best[1] <= f_limit:
        result, new_f = rbfs(best[0], row + 1, max_depth, min(f_limit, alternative))
        if result is not None:
            return result, new_f
        best[1] = new_f
        successors.sort(key=lambda x: x[1]) 
        best = successors[0]
        alternative = successors[1][1] if len(successors) > 1 else math.inf

    return None, best[1]

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1 or \
           (col - (row - i) >= 0 and board[i][col - (row - i)] == 1) or \
           (col + (row - i) < 8 and board[i][col + (row - i)] == 1):
            return False
    return True

def solve_n_queens(max_depth=8):
    board = [[0 for _ in range(8)] for _ in range(8)]
    solution, _ = rbfs(board, 0, max_depth, math.inf)
    if solution:
        for row in solution:
            print(row)
        print("Misplaced queens (heuristic F3):", f3(solution))
    else:
        print("No solution")

solve_n_queens()
