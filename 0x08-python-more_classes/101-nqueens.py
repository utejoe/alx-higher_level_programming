#!/usr/bin/python3

import sys


class NQueens:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def solve(self):
        self._solve([], 0)
        return self.solutions

    def _solve(self, queens, row):
        if row == self.n:
            self.solutions.append(queens)
            return

        for col in range(self.n):
            if self._is_valid(queens, row, col):
                self._solve(queens + [col], row + 1)

    def _is_valid(self, queens, row, col):
        for r, c in enumerate(queens):
            if c == col or r + c == row + col or r - c == row - col:
                return False
        return True


def print_solutions(solutions):
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


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

    nqueens = NQueens(n)
    solutions = nqueens.solve()
    print_solutions(solutions)
