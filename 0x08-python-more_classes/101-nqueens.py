#!/usr/bin/python3
import sys

def nqueens(n):
    solutions = []
    cols = []
    diag1 = []
    diag2 = []

    def backtrack(row):
        if row == n:
            solutions.append(cols[:])
        for col in range(n):
            if col not in cols and row - col not in diag1 and row + col not in diag2:
                cols.append(col)
                diag1.append(row - col)
                diag2.append(row + col)
                backtrack(row + 1)
                cols.pop()
                diag1.pop()
                diag2.pop()

    backtrack(0)
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
    solutions = nqueens(n)
    for sol in solutions:
        print([[i, sol[i]] for i in range(n)])
