from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            # Iterating over the items on the left row of the matrix
            self.dfs(i, 0, board)
            # Iterating over the items on the right row of the matrix
            self.dfs(i, n - 1, board)

        for j in range(n):
            # Iterating over the items on the top row of the matrix
            self.dfs(0, j, board)
            # Iterating over the items on the bottom row of the matrix
            self.dfs(m - 1, j, board)

        for i in range(m):
            for j in range(n):
                # We flip the Os of the surrounded regions
                if board[i][j] == "O":
                    board[i][j] = "X"
                # We preserve the "O" of the non-surrounded regions
                if board[i][j] == "-1":
                    board[i][j] = "O"

    def dfs(self, i, j, board):
        m = len(board)
        n = len(board[0])
        # Checking the boundaries of the matrix
        if (i < 0) or (i >= m) or (j < 0) or (j >= n):
            return
        # Checking that we are still in the "O" region
        if board[i][j] != "O":
            return
        # We mark the items of the non-surrounded region with -1
        board[i][j] = "-1"

        self.dfs(i - 1, j, board)
        self.dfs(i + 1, j, board)
        self.dfs(i, j - 1, board)
        self.dfs(i, j + 1, board)