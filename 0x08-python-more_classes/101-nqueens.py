import sys

def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve(board, row, n):
    # If all queens are placed, print the solution
    if row == n:
        print(board)
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n)
            board[row][col] = 0

def nqueens(n):
    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty chessboard
    board = [[0 for x in range(n)] for y in range(n)]

    # Solve the problem
    solve(board, 0, n)

# Check if the program was called with the correct arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Check if N is an integer
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

nqueens(n)
