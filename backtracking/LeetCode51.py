from typing import List, Tuple, Set


class Solution:
    # Time complexity: O(n^n)
    # Space complexity: O(n^3) if we consider the output, O(n) otherwise
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.boards = []
        self.n = n

        for j in range(self.n):
            self.solve_row(0, j, [], [])

        return self.boards

    def build_row_str(self, col: int):
        """
        Builds a row of the board.
        :param col: column where the queen is placed
        :return: a string representing the row
        """
        row_str = ""

        for k in range(self.n):
            if k == col:
                row_str += "Q"
                continue
            row_str += "."

        return row_str

    def get_forbidden_columns(self, row, placed_queens: List[Tuple[int, int]]):
        forbidden_cols = set()

        for i, j in placed_queens:
            delta = row + 1 - i
            # We cannot add two queens on the same column
            forbidden_cols.add(j)
            # We cannot add two queens on the same diagonal
            forbidden_cols.add(j + delta)
            forbidden_cols.add(j - delta)

        return forbidden_cols

    def solve_row(self, i: int, j: int, board: List[str], placed_queens: List[Tuple[int, int]]):
        board.append(self.build_row_str(j))

        if i == self.n - 1:
            self.boards.append(board.copy())
        else:
            placed_queens.append((i, j))

            forbidden_cols = self.get_forbidden_columns(i, placed_queens)

            for k in range(self.n):
                if k not in forbidden_cols:
                    self.solve_row(i + 1, k, board, placed_queens)

            placed_queens.pop()

        board.pop()
