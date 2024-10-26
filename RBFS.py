import random
import heapq


goal_solution = [
    (0, 0), (1, 4), (2, 7), (3, 5),
    (4, 2), (5, 6), (6, 1), (7, 3)
]

def generate_random_board():
    board = [[0 for _ in range(8)] for _ in range(8)]
    positions = set()
    
    while len(positions) < 8:
        row, col = random.randint(0, 7), random.randint(0, 7)
        if (row, col) not in positions:
            board[row][col] = 1
            positions.add((row, col))
    
    return board

def heuristic_f3(board):
    misplaced_queens = 0
    for goal_row, goal_col in goal_solution:
        if board[goal_row][goal_col] != 1:
            misplaced_queens += 1
    return misplaced_queens

def copy_board(board):
    return [row[:] for row in board]


def brfs(board):
    global iterations, nodes_expanded
    iterations = 0
    nodes_expanded = 0

    priority_queue = []
    heapq.heappush(priority_queue, (heuristic_f3(board), board))
    visited = set()

    while priority_queue:
        _, current_board = heapq.heappop(priority_queue)
        iterations += 1
        current_conflicts = heuristic_f3(current_board)
        
        if current_conflicts == 0:
            return current_board
        
        for col in range(8):
            current_row = next((row for row in range(8) if current_board[row][col] == 1), None)
            if current_row is None:
                continue

            for new_row in range(8):
                if new_row != current_row and current_board[new_row][col] == 0:
                    new_board = copy_board(current_board)
                    new_board[current_row][col] = 0
                    new_board[new_row][col] = 1
                    nodes_expanded += 1

                    board_tuple = tuple(tuple(row) for row in new_board)
                    if board_tuple not in visited:
                        visited.add(board_tuple)
                        heapq.heappush(priority_queue, (heuristic_f3(new_board), new_board))

            for new_col in range(8):
                if new_col != col and current_board[current_row][new_col] == 0:
                    new_board = copy_board(current_board)
                    new_board[current_row][col] = 0
                    new_board[current_row][new_col] = 1
                    nodes_expanded += 1

                    board_tuple = tuple(tuple(row) for row in new_board)
                    if board_tuple not in visited:
                        visited.add(board_tuple)
                        heapq.heappush(priority_queue, (heuristic_f3(new_board), new_board))

    return None

def solve_8_queens_with_brfs():
    global iterations, nodes_expanded
    iterations = 0
    nodes_expanded = 0

    board = generate_random_board()
    print("Init board:")
    print_board(board)

    solution = brfs(board)

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

solve_8_queens_with_brfs()
