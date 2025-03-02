from typing import List


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])

        self.cache = [[-1]*self.m for _ in range(self.n)]

        max_square = 0

        for i in range(self.n):
            for j in range(self.m):
                max_square = max(max_square, self.maximal_square(i, j)**2)

        return max_square

    def maximal_square(self, i, j):
        if (i > self.n - 1) or (j > self.m - 1):
            return 0

        if self.cache[i][j] != -1:
            return self.cache[i][j]

        if self.matrix[i][j] == "0":
            return 0

        self.cache[i][j] = 1 + min(
            self.maximal_square(i + 1, j),
            self.maximal_square(i + 1, j + 1),
            self.maximal_square(i, j + 1)
        )
        return self.cache[i][j]
