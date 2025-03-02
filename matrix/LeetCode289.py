from typing import List


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    def gameOfLife(self, board: List[List[int]]) -> None:
        self.board = board
        self.n = len(board)
        self.m = len(board[0])
        # Checking which cells will come into life again and which cells will die
        for i in range(self.n):
            for j in range(self.m):
                nb_living_neighbors = self.get_number_of_living_neighbors(i, j)
                # When a cell was dead and comes into life, we store a temporary 3 as a value
                if (board[i][j] == 0) and (nb_living_neighbors == 3):
                    board[i][j] = 3
                    continue
                # When a cell was alive and dies, we store a temporary 2 as a value
                if (board[i][j] == 1) and (nb_living_neighbors < 2 or nb_living_neighbors > 3):
                    board[i][j] = 2
        # Replacing twos and threes with zeroes and ones respectively before returning
        for i in range(self.n):
            for j in range(self.m):
                if (board[i][j] == 1) or (board[i][j] == 3):
                    board[i][j] = 1
                    continue
                board[i][j] = 0

    def get_number_of_living_neighbors(self, i, j):
        nb_living = 0

        nb_living += int(self.is_living(i - 1, j - 1))
        nb_living += int(self.is_living(i - 1, j))
        nb_living += int(self.is_living(i - 1, j + 1))
        nb_living += int(self.is_living(i, j + 1))
        nb_living += int(self.is_living(i + 1, j + 1))
        nb_living += int(self.is_living(i + 1, j))
        nb_living += int(self.is_living(i + 1, j - 1))
        nb_living += int(self.is_living(i, j - 1))

        return nb_living

    def is_living(self, i, j):
        # A neighbor is alive when it stores currently a one or if it was already processed, and a 2 was set as its
        # new value (it was alive, but it will be dead in the next iteration)
        return self.is_in_bounds(i, j) and ((self.board[i][j] == 1) or (self.board[i][j] == 2))

    def is_in_bounds(self, i, j):
        return (0 <= i <= self.n - 1) and (0 <= j <= self.m - 1)
