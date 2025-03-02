from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.grid = obstacleGrid
        self.n = len(obstacleGrid)
        self.m = len(obstacleGrid[0])
        self.cache = [[-1]*self.m for _ in range(self.n)]

        return self.dfs(0, 0)

    def dfs(self, i, j):
        # Got out of bounds or hit an obstacle
        if not self.is_in_bounds(i, j) or self.grid[i][j] == 1:
            return 0
        # Avoiding redundant computations by using memoization
        if self.cache[i][j] != -1:
            return self.cache[i][j]
        # Reached destination
        if (i == self.n - 1) and (j == self.m - 1):
            return 1

        paths_down = self.dfs(i + 1, j)
        paths_right = self.dfs(i, j + 1)

        self.cache[i][j] = paths_down + paths_right
        return self.cache[i][j]

    def is_in_bounds(self, i, j):
        return (0 <= i <= self.n - 1) and (0 <= j <= self.m - 1)
