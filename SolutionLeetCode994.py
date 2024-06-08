from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        nb_oranges = 0
        last_rotten_oranges = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    last_rotten_oranges.append((i, j))

                if grid[i][j] != 0:
                    nb_oranges += 1
        # Edge case: there are no oranges in the specified grid
        if nb_oranges == 0:
            return 0

        time_in_minutes = -1
        nb_of_rotten_oranges = 0

        while len(last_rotten_oranges) > 0:
            # Number of oranges to process
            k = len(last_rotten_oranges)

            for _ in range(k):
                i, j = last_rotten_oranges.popleft()
                self.bfs(i, j, grid, last_rotten_oranges)
                nb_of_rotten_oranges += 1

            time_in_minutes += 1

        return time_in_minutes if nb_of_rotten_oranges == nb_oranges else -1

    def bfs(self, i, j, grid, last_rotten_oranges):
        # Rotting neighbor oranges
        self.rot_neighbor(i - 1, j, grid, last_rotten_oranges)
        self.rot_neighbor(i + 1, j, grid, last_rotten_oranges)
        self.rot_neighbor(i, j - 1, grid, last_rotten_oranges)
        self.rot_neighbor(i, j + 1, grid, last_rotten_oranges)

    def rot_neighbor(self, i, j, grid, last_rotten_oranges):
        m = len(grid)
        n = len(grid[0])
        # Checking the grid boundaries and if there is a fresh orange at position i, j
        if (i >= 0) and (i < m) and (j >= 0) and (j < n) and grid[i][j] == 1:
            last_rotten_oranges.append((i, j))
            # Rotting an orange
            grid[i][j] = 2