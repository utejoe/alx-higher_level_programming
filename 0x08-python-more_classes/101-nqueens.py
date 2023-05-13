#!/usr/bin/python3
import sys

def is_valid(board, row, col):
    """Check if it's valid to place a queen at board[row][col]."""
    n = len(board)

    # Check this row on the left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j]:
            return False

    # It's valid to place a queen at board[row][col]
    return True

def n_queens_helper(n, board, col, result):
    """Recursive backtracking helper function for the N queens problem."""
    if col == n:
        # We found a solution, add it to the result
        result.append([[r, c] for r, c in enumerate(board)])
        return

    for row in range(n):
        if is_valid(board, row, col):
            # Place the queen at board[row][col]
            board[row][col] = 1

            # Explore further by placing the queens in the next columns
            n_queens_helper(n, board, col + 1, result)

            # Backtrack
            board[row][col] = 0

def n_queens(n):
    """Solve the N queens problem and return a list of solutions."""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty chessboard of size n x n
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Solve the N queens problem using recursive backtracking
    result = []
    n_queens_helper(n, board, 0, result)

    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = n_queens(n)
    for sol in solutions:
        print(sol)
