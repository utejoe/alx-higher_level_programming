import sys

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_n_queens(n):
    solutions = []
    def backtrack(board, col):
        if col == n:
            solutions.append(list(enumerate(board)))
            return
        for row in range(n):
            if is_safe(board, row, col):
                board[col] = row
                backtrack(board, col+1)
                board[col] = -1
    backtrack([-1]*n, 0)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = solve_n_queens(n)
    for solution in solutions:
        print(solution)
