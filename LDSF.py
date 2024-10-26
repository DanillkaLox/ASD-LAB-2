import random

def generate_random_board():
    board = [[0 for _ in range(8)] for _ in range(8)]
    positions = set()
    
    while len(positions) < 8:
        row, col = random.randint(0, 7), random.randint(0, 7)
        if (row, col) not in positions:
            board[row][col] = 1
            positions.add((row, col))
    
    return board

def count_conflicts(board):
    conflicts = 0
    for row in range(8):
        for col in range(8):
            if board[row][col] == 1:
                conflicts += count_conflicts_for_queen(board, row, col)
    return conflicts // 2

def count_conflicts_for_queen(board, row, col):
    conflicts = 0
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),  
        (1, -1), (1, 0), (1, 1)  
    ]
    
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < 8 and 0 <= c < 8:
            if board[r][c] == 1:
                conflicts += 1
            r += dr
            c += dc
    return conflicts

def copy_board(board):
    return [row[:] for row in board]

def ldfs(board, depth_limit, max_depth):
    global iterations, nodes_expanded
    iterations += 1

    current_conflicts = count_conflicts(board)
    if current_conflicts == 0:
        return board

    if depth_limit == 0:
        return None 
    
    for col in range(8):
        current_row = next((row for row in range(8) if board[row][col] == 1), None)
        if current_row is None:
            continue
        
        for new_row in range(8):
            if new_row != current_row and board[new_row][col] == 0:
                new_board = copy_board(board)
                new_board[current_row][col] = 0
                new_board[new_row][col] = 1
                nodes_expanded += 1
                
                if count_conflicts(new_board) < current_conflicts:
                    result = ldfs(new_board, depth_limit - 1, max_depth)
                    if result is not None:
                        return result

        for new_col in range(8):
            if new_col != col and board[current_row][new_col] == 0:
                new_board = copy_board(board)
                new_board[current_row][col] = 0
                new_board[current_row][new_col] = 1
                nodes_expanded += 1

                if count_conflicts(new_board) < current_conflicts:
                    result = ldfs(new_board, depth_limit - 1, max_depth)
                    if result is not None:
                        return result

    if depth_limit < max_depth:
        return ldfs(board, depth_limit + 1, max_depth)

    return None

def solve_8_queens_with_ldfs():
    global iterations, nodes_expanded
    iterations = 0
    nodes_expanded = 0

    board = generate_random_board()
    print("Init board:")
    print_board(board)

    depth_limit = 1
    max_depth = 4 
    solution = ldfs(board, depth_limit, max_depth)

    if solution is not None:
        print("\nSolution:")
        print_board(solution)
    else:
        print("\nNo solution found within specified depth.")

    print(f"\nIterations: {iterations}")
    print(f"Expanded nodes: {nodes_expanded}")

def print_board(board):
    for row in board:
        print(row)

solve_8_queens_with_ldfs()
