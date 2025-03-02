import sys
from typing import List


class Solution:
    # Time complexity: O(n*m)
    # Space complexity: O(n*m)
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid

        self.n = len(self.grid)
        self.m = len(self.grid[0])

        self.cache = [[-1]*self.m for _ in range(self.n)]

        return self.dfs(0, 0)

    def dfs(self, i, j):
        if self.cache[i][j] != -1:
            return self.cache[i][j]

        if (i == self.n - 1) and (j == self.m - 1):
            return self.grid[i][j]

        min_sum = sys.maxsize

        if i < self.n - 1:
            min_sum = min(min_sum, self.dfs(i + 1, j) + self.grid[i][j])

        if j < self.m - 1:
            min_sum = min(min_sum, self.dfs(i, j + 1) + self.grid[i][j])

        self.cache[i][j] = min_sum
        return min_sum