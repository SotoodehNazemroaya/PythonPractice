def is_safe(board, row, col, n):
    # Check column for conflicts
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def solve_n_queens(board, row, n, solutions):
    # If we have placed queens in all rows, it's a valid solution
    if row == n:
        solutions.append(board.copy())  # Store the valid board configuration
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # Place queen
            solve_n_queens(board, row + 1, n, solutions)  # Recur for next row
            board[row] = -1  # Backtrack: remove queen

def print_solutions(solutions, n):
    for solution in solutions:
        for i in range(n):
            row = ['.' for _ in range(n)]
            row[solution[i]] = 'Q'
            print(' '.join(row))
        print()

def n_queens(n):
    board = [-1] * n  # Initialize an empty board, -1 means no queen placed
    solutions = []
    
    solve_n_queens(board, 0, n, solutions)
    print_solutions(solutions, n)

# Example usage
n = 4  # Change this value to test with different board sizes
print(f"Solutions for {n}-Queens:")
n_queens(n)
