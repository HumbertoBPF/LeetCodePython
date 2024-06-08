from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        queue = deque()
        visited_cells = [[False]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    self.add_neighbor(i, j, 0, mat, queue, visited_cells)

        while len(queue) > 0:
            i, j, depth = queue.popleft()

            mat[i][j] = depth

            self.add_neighbor(i - 1, j, depth + 1, mat, queue, visited_cells)
            self.add_neighbor(i + 1, j, depth + 1, mat, queue, visited_cells)
            self.add_neighbor(i, j - 1, depth + 1, mat, queue, visited_cells)
            self.add_neighbor(i, j + 1, depth + 1, mat, queue, visited_cells)

        return mat

    def add_neighbor(self, i, j, depth, mat, queue, visited_cells):
        m = len(mat)
        n = len(mat[0])

        if (i < 0) or (i > m - 1) or (j < 0) or (j > n - 1):
            return

        if visited_cells[i][j]:
            return

        queue.append((i, j, depth))
        visited_cells[i][j] = True
