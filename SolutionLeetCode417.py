from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        accessible_from_atlantic = set()
        accessible_from_pacific = set()
        # Iterating over the rows
        for i in range(m):
            # Left border cells
            self.dfs(i, 0, -1, heights, accessible_from_pacific)
            # Right border cells
            self.dfs(i, n - 1, -1, heights, accessible_from_atlantic)

        # Iterating over the columns
        for i in range(n):
            # Top border cells
            self.dfs(0, i, -1, heights, accessible_from_pacific)
            # Bottom border cells
            self.dfs(m - 1, i, -1, heights, accessible_from_atlantic)

        accessible_from_both_oceans = accessible_from_pacific.intersection(accessible_from_atlantic)
        return [[i, j] for i, j in accessible_from_both_oceans]


    def dfs(self, i, j, previous_cell, heights, visited):
        """
        Get all the cells accessible from i, j
        :param i: row coordinate
        :param j: column coordinate
        :param previous_cell: cell that was visited previous to the current one
        :param heights: matrix with the heights
        :param visited: coordinates of the cells that have already been visited
        """
        m = len(heights)
        n = len(heights[0])
        # Checking the matrix dimensions
        if (i > m - 1) or (i < 0) or (j > n - 1) or (j < 0):
            return

        # We don't want to visit a cell twice
        if (i, j) in visited:
            return

        # The water doesn't flow from a lower point to a higher one
        if heights[i][j] < previous_cell:
            return

        visited.add((i, j))
        # Going up
        self.dfs(i - 1, j, heights[i][j], heights, visited)
        # Going down
        self.dfs(i + 1, j, heights[i][j], heights, visited)
        # Going left
        self.dfs(i, j - 1, heights[i][j], heights, visited)
        # Going right
        self.dfs(i, j + 1, heights[i][j], heights, visited)