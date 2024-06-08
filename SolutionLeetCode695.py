from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        cache = {"area": 0, "max_area": 0}

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cache["area"] = 0

                    self.dfs(i, j, grid, cache)

                    if cache["area"] > cache["max_area"]:
                        cache["max_area"] = cache["area"]

        return cache["max_area"]

    def dfs(self, i, j, grid, cache):
        m = len(grid)
        n = len(grid[0])
        # Checking if we are still in the boundaries of the grid
        if (i < 0) or (i >= m) or (j < 0) or (j >= n):
            return
        # Checking that the current position is not an island (value = "0") or has already been visited (value = -1)
        if grid[i][j] != 1:
            return
        # Mark the position as visited and increment the area by one
        grid[i][j] = -1
        cache["area"] += 1
        # Visiting the vertical and horizontal neighbors
        self.dfs(i - 1, j, grid, cache)
        self.dfs(i + 1, j, grid, cache)
        self.dfs(i, j - 1, grid, cache)
        self.dfs(i, j + 1, grid, cache)
